# 作者:meedy
# 编写时间：2023/10/13  11:09
# 代码内容：登录购物网站
import requests
import urllib
from utils.utilsrequests import reqests_get
def user_info():
#第一步登录，拿到token
    url1 = 'http://admin.5istudy.online/login/'
    data =  {
        "username": '13811200000',
        "password": '123456'
    }

    r = requests.post(url1,json=data)
    #print(r.json())
    #print(r.json()["token"])
    token = r.json()["token"]
#第二部获取用户基本信息
    url = 'http://admin.5istudy.online/users/1/'

    headers ={'Authorization':'JWT '+ token }
    #print(headers)
    #s = requests.get(url,headers=headers)
    s = reqests_get(url,headers)
    print(s)
if __name__ == '__main__':

    user_info()

