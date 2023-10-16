# 作者:meedy
# 编写时间：2023/10/13  11:09
# 代码内容：登录购物网站
import requests
import urllib
from utils.utilsrequests import reqests_post
from utils.utilsrequests import Request
def login():

    url = 'http://admin.5istudy.online/login/'
    data =  {
        "username": '13811200000',
        "password": '123456'
    }

    #r = requests.post(url,json=data)
    #r = reqests_post(url,json=data)
    request = Request()
    r = request.post(url,json=data)

    print(r)
    print(type(r))

if __name__ == '__main__':
    login()
