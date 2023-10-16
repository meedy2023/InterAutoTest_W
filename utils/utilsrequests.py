# 作者:meedy
# 编写时间：2023/10/13  13:28
# 代码内容：requests方法封装
#1第一步：创建封装request.get()方法
import requests

def reqests_get(url,headers=None,json=None):
    r = requests.get(url,headers=headers)
    code = r.status_code
    try:

        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res["code"] = code
    res["body"] = body
    return  res

def reqests_post(url,json=None,headers=None):
    r = requests.post(url,json=json,headers=headers)
    code = r.status_code
    try:

        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res["code"] = code
    res["body"] = body
    return  res


class Request:
    def requests_api(self,url,json=None,headers=None,method='get'):
        if method == 'get':
            r = requests.get(url,json=json,headers=headers)
        elif method == 'post':
            r = requests.post(url,json=json,headers=headers)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res

    def get(self,url,**kwargs):

     return self.requests_api(url,method="get",**kwargs)

    def post(self,url,**kwargs):

     return self.requests_api(url,method="post",**kwargs)