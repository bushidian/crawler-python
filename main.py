import sites.ifeng.tech as tech
from core.models.config import config

import json

def main():

	print('程序启动')
	
	setting = loadingConfig()
	
	tech.crawler(setting)

	print('程序关闭')

def loadingConfig():
	
	with open('config.json') as file:
		data = json.load(file)
		return config(data['storeApi'])
	
if __name__ == '__main__':
	main()
