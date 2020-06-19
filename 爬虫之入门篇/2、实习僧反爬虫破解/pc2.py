import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36"
}
def detial_url(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,"lxml")
    title = soup.title.text
    company_name =soup.select(".com_intro .com-name ")[0].text
    salary= soup.select(".job_money.cutom_font")[0].text.encode("utf-8")
    salary = salary.replace(b"\xef\x92\xa6",b"1")
    salary = salary.replace(b"\xef\x84\xbf",b"5")
    salary = salary.replace(b"\xef\x84\xbf",b"0")
    salary = salary.decode()
    print(title,company_name,salary)

def crawl():
    for page in range(1,2):
        html = requests.get("https://www.shixiseng.com/interns?page={}&keyword=python".format(page),headers=headers)
        soup = BeautifulSoup(html.text,"lxml")
        offers = soup.select(".intern-wrap.intern-item")
        for offer in offers:
            url = offer.select(".f-l.intern-detail__job a")[0]["href"]
            detial_url(url)

crawl()
