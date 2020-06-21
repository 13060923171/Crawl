import requests
from uuid import uuid4
from urllib.parse import quote
import os
import time
from concurrent.futures import ThreadPoolExecutor
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36",
    "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&oq=%E7%BE%8E%E5%A5%B3&rsp=-1",
    "Cookie": "BDqhfp=%E7%BE%8E%E5%A5%B3%26%260-10-1undefined%26%261576%26%263; BIDUPSID=55B9F89BBD8CE76842ADD9DCE4E07064; PSTM=1588574309; BAIDUID=55B9F89BBD8CE76850CAB1E8E50293E6:FG=1; cflag=13%3A3; BDUSS=kxVN2lhTmEzVFVKcGU2UjMtfmhEV25ZVkRkazdRS2hhNHdQbUx4MmlVaVB2ZGxlSVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI8wsl6PMLJea; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.google.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E7%BE%8E%E5%A5%B3%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm"
}
#初始化一些参数，方便更好的调用
session = requests.session()
session.headers = headers
def get_img(url):
    html = session.get(url)
    #构造一个多线程池，就10个线程把
    threadingPool = ThreadPoolExecutor(max_workers=10)
    #为什么这里要用到防错机制，因为如果是用json的话，有一些图片可能会失败，要想全部成功获得，只有正则才行
    try:
        #定位它的内容
        content = html.json()['data']
        #用循环叠带把这些内容给打印出来
        for c in content[:-1]:
            #输出它的URL
            print(c['middleURL'])
            #用多线程来下载这些图片，从而提升我们的下载速度，达到我们的目的
            threadingPool.submit(download,url)
    except:
        pass

def download(imgurl):
    filename = '图片保存文件'
    #创建一个文件夹，如果这个文件夹不存在，那么我们就创建这个文件夹，这个是一条死语句，必须得背下来
    if not os.path.exists(filename):
        os.makedirs(filename)
    #获取这个图片的URL
    image = session.get(imgurl)
    #uuid4只是为了更好的命名而已，毕竟那么多图片，不可能一个个命名
    with open("图片保存文件/{}.jpg".format(uuid4()),"wb") as f:
        f.write(image.content)

def main():
    KEYWORD = input("请输入你要下载的图片内容：")
    for i in range(30,300,30):
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn={}&rn=30&gsm=96&1589535866384=". \
            format(quote(KEYWORD), quote(KEYWORD), i)
        get_img(url)

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)


