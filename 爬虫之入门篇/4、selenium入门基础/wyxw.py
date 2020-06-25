from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery
import json

browser = webdriver.Chrome("C:\\Users\\96075\\Desktop\\作业文档\\Python\\爬虫\\chromedriver.exe")
wait = WebDriverWait(browser,10)

def crawl_page():
    while True:
        try:
            while True:
                url = "https://news.163.com/"
                browser.get(url)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".mod_top_news2 li a")))
                get_products()
        except:
            crawl_page()

def get_products():
    html = browser.page_source
    doc = PyQuery(html)
    items = doc(".mod_top_news2 li a").items()
    for item in items:
        product = {
            "laiyuan":item.find("a#ne_article_source").text(),
            "wenzi":item.find("div#endText.post_text p").text(),
            "img":item.find("div#endText.post_text img").attr(),
            "title":item.find(".post_content_main h1").text(),
        }
        print(product)
        save_to_file(product)


def save_to_file(result):
    with open("zuoye.txt","w",encoding="UTF-8") as f:
        f.write(json.dump(result,ensure_ascii=False)+"\n")
        print("成功保存到txt中")


if __name__ == '__main__':
    crawl_page()

