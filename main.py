import sites.ifeng.tech as tech
import sites.leet.shh as shh
import sites.mt.esf as esf
from core.models.config import config
import utils.http as http

import json

def main():

    print('程序启动')

    setting = loadConfig()
    
    tech.crawler(setting)
    
    esf.crawler(setting)
    
    #shh.crawler(setting)

    print('程序关闭')


def loadConfig():

    with open('config.json') as file:
        data = json.load(file)
        return config(data['storeApi'])


if __name__ == '__main__':
    main()
