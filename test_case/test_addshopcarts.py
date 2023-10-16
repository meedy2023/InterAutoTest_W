# 作者:meedy
# 编写时间：2023/10/13  12:41
# 代码内容：实现加入购物车
import requests
import urllib
from utils.utilsrequests import reqests_post
from utils.utilsrequests import reqests_get
from utils.utilsrequests import Request

def shopcarts():
    # 第一步登录，拿到token
    url1 = 'http://admin.5istudy.online/login/'
    data = {
        "username": '13811200000',
        "password": '123456'
    }

    #r = requests.post(url1, json=data)
    #r = reqests_post(url1, json=data)
    request = Request()
    r = request.post(url1, json=data)
    # print(r.json())
    #print(r)
    token = r["body"]["token"]
    print(token)
    #第二部加入购物车
    url= 'http://admin.5istudy.online/shopcarts/'
    headers = {'Authorization': 'JWT ' + token}
    data = {
        'nums':'6',
        'goods':'3'
    }
    #r = requests.post(url,headers=headers,json=data)
    #r =  reqests_post(url,headers=headers,json=data)
    request = Request()
    r = request.post(url,headers=headers,json=data)
    print(r)
if __name__ == '__main__':
    shopcarts()
