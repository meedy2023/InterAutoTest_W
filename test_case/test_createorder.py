# 作者:meedy
# 编写时间：2023/10/13  12:41
# 代码内容：购物车
import requests
import urllib

def createorder():
    # 第一步登录，拿到token
    url1 = 'http://admin.5istudy.online/login/'
    data = {
        "username": '13811200000',
        "password": '123456'
    }

    r = requests.post(url1, json=data)
    # print(r.json())
    print(r.json()["token"])
    token = r.json()["token"]
    #第二部加入购物车
    url2= 'http://admin.5istudy.online/shopcarts/'
    headers = {'Authorization': 'JWT ' + token}
    data = {
        'nums':'6',
        'goods':'3'
    }
    r = requests.post(url2,headers=headers,json=data)
    print(r.json())
    #第三部创建订单
    url = 'http://admin.5istudy.online/orders/'
    data = {
        "post_script":"balabala",
        "order_mount": float('5303'),
        "address":"北京市 北京城区 东城区 北京市",
        "signer_name":"淘宝",
        "singer_mobile": '13811200000'
    }
    r = requests.post(url,headers=headers,json=data)
    print(r.json())

if __name__ == '__main__':
    createorder()