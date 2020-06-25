import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
headers = {
    'cookie': '_zap=d8ac8fe4-92c3-43c6-a6e5-dd61d19e7814; d_c0="ABBW_52tNhGPTrpAk5sMQG8ejVDwhvtXQOg=|1588507167"; _ga=GA1.2.1208007031.1589167171; _xsrf=izdfujUw7llwidje32HYIslLc9oWwN5o; capsion_ticket="2|1:0|10:1590838272|14:capsion_ticket|44:MDMyODFkYzhiMmVhNGViNDhlZDY1N2E4YTY3NWE4OGU=|b0e32e319aa78851e7a6e4d9c100090cdbbce38ff35d47252795d9047b71055a"; _gid=GA1.2.247287547.1592382369; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590331945,1590498592,1590838240,1592382372; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1592382372; SESSIONID=aviD6xPDj4AgfRh8JDX22j7wSrbkQgEkqwBXTfsBfat; KLBRSID=57358d62405ef24305120316801fd92a|1592382375|1592382367; JOID=VF8XAEmvIoK58dpOZKqHl5Gssztxz1Hq_MOjGyHBF8bflownWQz1a-L03kpksTcemiMZzoYWaL410cPoh-fDOIk=; osd=W1AdC0OgLYiy-9VBbqGNmJ6muDF-wFvh9sysESrLGMnVnYYoVgb-Ye371EFuvjgUkSkWwYwdYrE628jiiOjJM4M=',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
ids = re.compile('"cardId":"Q_(\d+)"',re.S|re.I)
re_content = re.compile('"excerptArea":{"text":"(.*?)"')

async def get_html():
    url = "https://www.zhihu.com/billboard"
    async with aiohttp.ClientSession(headers = headers) as session:
        async with session.get(url) as resp:
            print("知乎热榜状态码",resp.status)
            text = await resp.text()
    soup = BeautifulSoup(text,'lxml')
    #用正则表达式获取我们需要的信息
    contects = soup.select(".HotList-item")
    for contect in contects:
        title = contect.select_one(".HotList-itemTitle").text
        print(title)
    contents = re_content.findall(text)
    for c in contents:
        print(c)
        print("-"*30)
    hot_ids = ids.findall(text)
    for u in hot_ids:
        url = "https://www.zhihu.com/question/{}?utm_division=hot_list_page".format(u)
        print(url)


if __name__ == '__main__':
    loop =asyncio.get_event_loop()
    loop.run_until_complete(get_html())
    loop.close()



