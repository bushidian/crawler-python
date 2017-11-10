import sites.ifeng.tech as tech
from core.models.config import config
import utils.http as http

import json
import requests


def main():

    print('程序启动')

    setting = loadingConfig()

    r = http.get('http://www.baidu.com', { 'q': '我们' })
    print(r)
    
    # tech.crawler(setting)

    print('程序关闭')


def loadingConfig():

    with open('config.json') as file:
        data = json.load(file)
        return config(data['storeApi'])


if __name__ == '__main__':
    main()
