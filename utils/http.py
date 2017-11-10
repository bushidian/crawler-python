import requests

# 参考 http://blog.csdn.net/onlyanyz/article/details/45368841


def get(url, params=None):
    try:
        r = requests.get(url, params=params)
        if r.status_code != 200:
            print('请求: ' + url + ' 失败,错误代码:' + str(r.status_code))
        return r.text
    except:
        print('请求: ' + url + ' 失败, 请检查链接')


def post(url, body=None):

    try:
        r = requests.post(url, data=body)
        if r.status_code != 200:
            print('提交请求: ' + url + ' 失败,错误代码:' + str(r.status_code))
        return r.text
    except Exception as e:
        print('提交请求: ' + url + ' 失败, ' + str(e))
        return None


def put(url, body=None):

    try:
        r = requests.put(url, body)
        if r.status_code != 200:
            print('更改请求: ' + url + ' 失败,错误代码:' + str(r.status_code))
            return r.text
    except:
        print('更改请求: ' + url + ' 失败, 请检查链接')
        return None


def delete(url, body=None):
    try:
        r = requests.delete(url, body)
        if r.status_code != 200:
            print('删除请求: ' + url + ' 失败，错误代码:' + str(r.status_code))
        return r.text
    except:
        print('删除请求: ' + url + ' 失败, 请检查链接')
        return None
