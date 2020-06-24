# 关于爬虫，我们经常用到这4个解析库，最低要求是必须掌握2个解析库

# 1、python的编码解码，最常用到的就是utf-8了，不区分大小写

```python
text = "这是一段文本"
#encode是编码的意思，就是把text的内容转化为16位进制，给计算机看的
html = text.encode("utf8")
print(html)
#b'\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe6\xae\xb5\xe6\x96\x87\xe6\x9c\xac'
#decode是解码的意思，就是把上面这一串16位进制的东西，转化给我们看的
html = html.decode('utf8')
print(html)
#这是一段文本

```

注意他们有映射关系，就是内容必须一样，或者encode或者decode里面用的必须是同一个东西才行，不然会报错，一般utf8多用于保存

# 2、python的requests库这个是python的第三方库，是请求这个页面的意思，一般多用于和其他解析库配合着使用，是学爬虫必须掌握和最常用的库

```python
#基本框架
import requests 
url = "网站"
html = requests.get(post)(url)
print(html.text)
就这几条语句就可以直接把整个网页的信息爬取下来了，是不是很神奇
```

# 3.正则表达式，这个是最古老的一个库了，很多东西，当你很难获取的时候，我们首先考虑的就是正则表达式了，没有什么东西是正则获取不了的，如果你获取失败只能说明你的代码错了而已

```python
#正则最常用到的框架
import re
import requests 
url = "网站"
reponse = requests.get(post)(url)
t = reponse.text
#re.I使匹配对大小写不敏感，re.S使匹配包括换行在内的所有字符，这是我们最常用的
html = re.compile('(.*?)',re.I|re.S)
result = html.findall(t)
print(result)
```

# 4.python的解析器（正则>xpath>BeautifulSoup>pyquery）

```python
#xpath案例，爬取无广告的百度
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
headers = {
    "Cookie": "BIDUPSID=55B9F89BBD8CE76842ADD9DCE4E07064; PSTM=1588574309; BAIDUID=55B9F89BBD8CE76850CAB1E8E50293E6:FG=1; BDUSS=kxVN2lhTmEzVFVKcGU2UjMtfmhEV25ZVkRkazdRS2hhNHdQbUx4MmlVaVB2ZGxlSVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI8wsl6PMLJea; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31358_1452_31326_21078_31590_31270_31661_31463_30823; delPer=0; PSINO=1; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BCLID=9040746557493305278; BDSFRCVID=R7DOJeC62uipA3rukmCN2bvZ_tw606QTH6aok-m-gl6dGKGK3xZmEG0PeM8g0KubhaS4ogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJPDVI82JCD3j-5cbjAWq4tehHRNtM39WDTm_Doa24JNhPoGMPcTX6DV5R6d-n-qtncI-pPKKR7OKJCzbPk-bM-UQP4ehpTL3mkjbn5zfn02OP5PM-Q6j-4syP4eKMRnWnnRKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5uajjcP",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36"
}
def get_baidu(url):
    html = requests.get(url,headers= headers)
    if html.status_code == 200:
        parse_html(html.text)
    else:
        print("error")

def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    results = soup.select("div.result.c-container")
    for r in results:
        title = r.select_one("h3 a").text
        href = r.select_one("h3 a")["href"]
        content = r.select_one("div.c-abstract").text
        print(title,href)
        print(content)

if __name__ == '__main__':
    KEYWORD = quote(input("请输入你要搜索的内容:"))
    url = "https://www.baidu.com/s?wd={}".format(KEYWORD)
    get_baidu(url)

```

![xpath语法](https://s1.ax1x.com/2020/06/24/NaTTln.png)