import datetime
import utils.http as http
import json


def save(config, page):
    
    url = config.storeApi

    res = http.post(url, page.toDict())

    data = res
