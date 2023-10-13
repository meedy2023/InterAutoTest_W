# 作者:meedy
# 编写时间：2023/10/13  11:09
# 代码内容：登录购物网站
import requests
import urllib
#第1部分获取商品列表信息
def goods_list():
    url= 'http://admin.5istudy.online/goods/'
    data ={
        'page':'1',
        'pricemin':'',
        'pricemax':'',
        'is_hot':'1',
        'is_new':'0',
        'top_category':'1',
        'search':'',
        'ordering':'-add_time'
    }
    r = requests.get(url,json=data)
    print(r.json())

if __name__ == '__main__':
    goods_list()

