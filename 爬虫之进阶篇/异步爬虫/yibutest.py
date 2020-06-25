import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}

async def crawl(i):
    url = "https://www.qiushibaike.com/text/page/{}/".format(i)
    async with aiohttp.ClientSession(headers = headers) as session:
        async with session.get(url) as resp:
            print(resp.status)
            text = await resp.text()
            print('start',i)
    soup = BeautifulSoup(text,'lxml')
    lis = soup.select("div.content")
    for li in lis:
        print(li.get_text())

if __name__ == '__main__':
    s = time.time()
    loop = asyncio.get_event_loop()
    tasks = [crawl(i) for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-s)
    loop.close()