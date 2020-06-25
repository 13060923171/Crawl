import json

import requests
import xlwt

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36"
}

def get_html():
    html = requests.get(url = "https://news.qq.com/ext2020/apub/json/prevent.new.json",headers=headers)
    content = json.loads(html.text)
    for c in content:
        id = c["id"]
        title = c["title"]
        print(id,title)
        write_txt(c)
        write_cvs(c)

def write_txt(result):
    with open("write_txt.txt","a+",encoding="utf-8") as f:
        f.write(json.dumps(result,ensure_ascii=False)+"\n")
        print("成功保存到TXT文本中")

def write_cvs(result):
    with open("write_csv.csv","a+",encoding="utf-8") as f:
        f.write(json.dumps(result,ensure_ascii=False)+"\n")
        print("成功保存到csv文本中")

def write_cvs(result):
    with open("write_csv.xls", "a+", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")
        print("成功保存到xls文本中")

def create_excel():
    Excel_book = xlwt.Workbook()
    sheet = Excel_book.add_sheet("hello")
    sheet.write(1,0,"hello")
    Excel_book.save("hello.xls")



if __name__ == '__main__':
    get_html()
    create_excel()