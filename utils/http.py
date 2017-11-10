import requests

#参考 http://blog.csdn.net/onlyanyz/article/details/45368841

def get(url, params = None):
    
    r = requests.get(url, params = params)
    if r.status_code != 200:
        print('请求: ' + url + '失败,错误代码:' + r.status_code)
    else:
       return r.text

def post(url, data = None):
    
    r = requests.post(url, data = data)
    if r.status_code != 200:
        print('提交请求: ' + url + '失败,错误代码:' + r.status_code)
    else 
        return r.text
        
def put(url, data = None):
    
    r = requests.put(url, data)
    if r.status_code != 200:
        print('更改请求: ' + url + '失败,错误代码:' + r.status_code)
    else 
        return r.text
    
def delete(url, data = None):
    
    r = requests.delete(url, data)
    if r.status_code != 200:
        print('删除请求: ' + url + '失败，错误代码:' + r.status_code)
    else:
        return r.text