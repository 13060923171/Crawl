import requests
from bs4 import BeautifulSoup
import multiprocessing
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Referer': 'https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4830389020085397&output=html&h=250&slotname=1983604743&adk=2912570974&adf=1831147650&w=300&lmt=1590915729&psa=1&guci=2.2.0.0.2.2.0.0&format=300x250&url=https%3A%2F%2Fbook.douban.com%2Ftag%2F%25E6%25AD%25A6%25E4%25BE%25A0&flash=0&wgl=1&dt=1590915729035&bpp=10&bdt=395&idt=35&shv=r20200526&cbv=r20190131&ptt=9&saldr=aa&abxe=1&cookie=ID%3Ddd6d7a4429360535%3AT%3D1585750322%3AS%3DALNI_MamjD8UWHvKyVyTKPKwltr6RvqM8Q&crv=1&correlator=4116616863202&frm=20&pv=2&ga_vid=1355082980.1588561648&ga_sid=1590913367&ga_hid=1530581719&ga_fc=1&iag=0&icsg=8389128&dssz=24&mdo=0&mso=0&u_tz=480&u_his=4&u_java=0&u_h=900&u_w=1440&u_ah=797&u_aw=1440&u_cd=24&u_nplug=3&u_nmime=4&adx=940&ady=247&biw=1440&bih=240&scr_x=0&scr_y=0&eid=21065531%2C21066085%2C42530451%2C42530453&oid=3&pvsid=3730255798050151&pem=640&ref=https%3A%2F%2Fbook.douban.com%2F&rx=0&eae=0&fc=896&brdim=0%2C23%2C0%2C23%2C1440%2C23%2C1440%2C797%2C1440%2C240&vis=1&rsz=%7C%7CoeEbr%7C&abl=CS&pfx=0&fu=8216&bc=31&ifi=1&uci=a!1&btvi=1&fsb=1&xpc=eNJGycNzxM&p=https%3A//book.douban.com&dtd=71'
}

def get_link(html):
    print('获取书的父进程为：{}'.format(multiprocessing.current_process().pid))
    soup = BeautifulSoup(html.text,'lxml')
    title = soup.select_one('#wrapper h1 span').text
    print(title)

#解析豆瓣
def get_html(url):
    print('html当前进程为{}'.format(multiprocessing.current_process().pid))
    html = requests.get(url,headers =headers)
    #建立一个线程池，设置3个线程
    threadpools = ThreadPoolExecutor(max_workers = 3)
    soup = BeautifulSoup(html.text,'lxml')
    urls = soup.select('li.subject-item h2 a')
    #获取每一本书里面的url
    for url in urls:
        link = url['href']
        #当获取这个URL之后再去获取这个url的信息
        html = requests.get(link, headers=headers)
        if html.status_code == 200:
            #如果状态码为200则使用线程池调用get_link这个函数，参数为html
            threadpools.submit(get_link, html)
        else:
            print('Error')

if __name__ == '__main__':
    urls = [
        'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
        'https://book.douban.com/tag/%E6%BC%AB%E7%94%BB',
        'https://book.douban.com/tag/%E6%AD%A6%E4%BE%A0'
    ]
    #设置进程池，创建3个进程，当你开3个进程的时候就相当于开3个程序，3个程序里面包含了3个线程，就相当于3个程序里面再加了3个加速器
    #这样就用最快的速度去执行，但是得注意你进程和你的CPU有关，4核的CPU最好好4个进程就好了
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(get_html, url) for url in urls]