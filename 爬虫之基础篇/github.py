import requests
import time
from bs4 import BeautifulSoup
headers= {
    "Referer": "https://github.com/login",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.62 Safari/537.36",
    "Cookie":"octo=GH1.1.797596467.1588574662; _device_id=1e4c99f5bfe1dd7f5af98ff975917802; _ga=GA1.2.358056422.1588867886; has_recent_activity=1; logged_in=no; _gh_sess=zo5JkLOQcw9QrolKtHPVtAkU2PBB6Cs8C0rsirXgkQuxMghn7uqC33tEWjtlmJEIbYiatTVCgt%2FyN3Jj1%2FjPkI7wLRwhDfKbm4gdZXQTCERCeV2tcepEQqtCe7hilZfSngCvUWhUllpLxTrUMAcQZz7EL7RlmA50FJJ0rf07xsyAooUVmo6QPZEUD3y4TNP4Bnw0qujVTsQmNFL1O4vD2Q%2FGU4XshYFgs9bpn6ZDMm2dqrYhbCzRwe3kYXmZQL6GMShpJ3tkiEk7Ku4%2FtV97fg%3D%3D--RPSZb0UjUhruZnoa--6sx16kg7GkDu59sIJEQfXA%3D%3D; tz=Asia%2FShanghai"
}
#保存我们获取页面的信息，编码格式就用utf-8防止出错
def save_html(html):
    with open("login.html","w",encoding="utf-8") as f:
        f.write(html)
#定义我们的参数，个人写法问题，影响不大
session = requests.session()
session.headers = headers
#这里我们用到的是请求方法，因为首先要先进去这个网页必须要登录，既然是登录那么就要用到post请求，伪装成个人登录
def post_github():
    url = "https://github.com/session"
    data = {
        "commit": "Sign in",
        "authenticity_token": "//iIOVmz1V4Wqn56ZUIUjcxTIv+BDF82Rikip5A4jjDQyYsXIvnstcZBD5brxwn8MSslJN6UhexSJLZv11F0NA==",
        "login": "你自己的账户",
        "password": "账户密码",
        "webauthn-support": "supported",
        "webauthn-iuvpaa-support": "supported",
        "timestamp": "{}".format(time.time()),
        "timestamp_secret": "1375d71bc5bff1e53426d150e18626ab420be7c14cd84fec7f916cf19f225d07",
    }
    html = session.post(url,headers=headers,data = data)
    if html.status_code == 200:
        print('feeding....')
        get_feed(session)
    else:
        print(html.status_code)
#请求成功之后，就是获取这个页面的信息了
def get_feed(sess):
        html = sess.get('https://github.com/dashboard-feed')
        soup = BeautifulSoup(html.text,'lxml')
        content = soup.select('div.watch_started')
        #把内容循环叠带，一个个打印出来
        for c in content:
            try:
                from_people = c.select('.d-flex.flex-items-baseline div div div div a')[0].text
                to_people = c.select('.d-flex.flex-items-baseline div div div div a')[1].text
                code = c.select('.d-flex.flex-items-baseline span.ml-0 span')[1].text
                print(from_people,to_people,code)
                #打印出来的信息之后就用保存函数，把它们全部保存下来
                save_data("from:{} to:{} data:{}\n".format(from_people,to_people,code))
            except:
                pass
def save_data(row):
    with open('github_data.txt','a+',encoding='utf8')as f:
        f.write(row)
if __name__ == '__main__':
    post_github()