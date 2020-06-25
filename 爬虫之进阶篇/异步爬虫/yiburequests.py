import asyncio,requests
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}
#先用requests正常获取我们想要的数据
def crawl(i):
    print("正在爬取",i)
    url = "https://www.qiushibaike.com/text/page/{}/".format(i)
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    lis = soup.select('div.content')
    for li in lis:
        print(li.get_text())
#开始调用我们的异步函数
async def main():
    #先开启我们的异步函数
    loop = asyncio.get_event_loop()
    #创建一个列表，用来存放我们的线程
    tasks = []
    #创建线程池，设置10个线程
    with ThreadPoolExecutor(max_workers = 10) as t:
        #循环10次，我们的异步函数
        for i in range(10):
            #开启我们的异步，先确定我们的要执行这个任务，在哪里执行，在我们的线程池执行，执行我们的crawl这个函数，变量为i
            tasks.append(loop.run_in_executor(t,crawl,i))

if __name__ == '__main__':
    s = time.time()
    #开启我们的异步函数
    loop = asyncio.get_event_loop()
    #等到我们的异步执行完毕
    loop.run_until_complete(main())
    print(time.time()-s)
    #关闭我们的异步
    loop.close()