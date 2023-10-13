# 作者:meedy
# 编写时间：2023/10/13  11:09
# 代码内容：登录购物网站
import requests
import urllib
def user_info():
#第一步登录，拿到token
    url1 = 'http://admin.5istudy.online/login/'
    data =  {
        "username": '13811200000',
        "password": '123456'
    }

    r = requests.post(url1,json=data)
    #print(r.json())
    print(r.json()["token"])
    token = r.json()["token"]
#第二部获取用户基本信息
    url2 = 'http://admin.5istudy.online/users/1/'

    headers ={'Authorization':'JWT '+ token }
    s = requests.get(url2,headers=headers)
    print(s.json())
if __name__ == '__main__':

    user_info()

