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
