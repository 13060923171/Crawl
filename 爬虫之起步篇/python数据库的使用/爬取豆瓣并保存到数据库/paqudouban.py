from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
import os
from doubanzhishujuku import Book,sess
import asyncio
import aiohttp
import time
headers = {
    "Referer": "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36",
    "Cookie": "ll='118281'; bid=O7ufDRQf-EM; ap_v=0,6.0; __utma=30149280.824434074.1589705958.1589705958.1589705958.1; __utmc=30149280; __utmz=30149280.1589705958.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=81379588.1042792723.1589705961.1589705961.1589705961.1; __utmc=81379588; __utmz=81379588.1589705961.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; gr_user_id=fe84be7b-7be1-48cd-96b7-db1a1bcb1df7; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=8a7d4654-db1a-4780-a80d-426a80bb2eba; gr_cs1_8a7d4654-db1a-4780-a80d-426a80bb2eba=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1589705961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_8a7d4654-db1a-4780-a80d-426a80bb2eba=true; _pk_id.100001.3ac3=e2ddd2d20afe5226.1589705961.1.1589705990.1589705961.; __utmb=30149280.5.10.1589705958; __utmb=81379588.4.10.1589705961"
}
#这里采用异步，为了可以更快的爬取，保存
async def parse_html(i):
    url = "https://book.douban.com/tag/{}?start={}&type=T".format(quote(KEYWORD), i)
    #固定写法，定义它的请求头并且把它们设为session
    async with aiohttp.ClientSession(headers = headers) as session:
        #去获取这个url并且把它作为resp
        async with session.get(url) as resp:
            #打印爬取的状态码是否是200
            print("豆瓣的状态码", resp.status)
            #并且把他们保存到文本里面
            text = await resp.text()
    try:
        #这些就是以往的写法了没什么好说的，这里用到的是BeautifulSoup解析器
        soup = BeautifulSoup(text,"lxml")
        books = soup.select("li.subject-item")
        for book in books:
            title = book.select_one(".info h2 a").text.strip().replace(" :","").replace(" ","").replace("\n","")
            info = book.select_one(".info div.pub").text.strip().replace("\n","")
            star = book.select_one("span.rating_nums").text
            pingfeng = book.select_one("span.pl").text.strip().replace("\n","")
            text = book.select_one(".info p").text
            img = book.select_one("img")["src"]
            print(title,info,star,pingfeng,img)
            print(text)
            print("="*50)

            #插入数据库
            book_data = Book(
                title = title,
                info = info,
                star = star,
                pingfeng = pingfeng,
                text = text,
            )
            #全部添加到数据库里面
            sess.add(book_data)
            #连接数据库
            sess.commit()
    except Exception as e:
        print(e)
        #如果出错了就回滚到原来的地方
        sess.rollback()
def download(title,url):
    if not os.path.exists("豆瓣图书图片"):
        os.makedirs("豆瓣图书图片")

    html = requests.get(url,headers=headers)
    with open("豆瓣图书图片/{}.jpg".format(title),"wb") as f:
        f.write(html.content)

if __name__ == '__main__':
    KEYWORD = input("请输入你要查询类型：")
    start = time.time()
    #固定写法，打开异步
    loop = asyncio.get_event_loop()
    #设置爬取的页数
    tasks = [parse_html(i) for i in range(0,100,20)]
    #爬取全部内容，等待结束
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start)
    #关闭
    loop.close()
