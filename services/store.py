import datetime
import utils.http as http
import json


def save(config, page):
    
    if not config.enableStore:
        return
    
    url = config.storeApi

    res = http.post(url, page.toDict())

    data = res
