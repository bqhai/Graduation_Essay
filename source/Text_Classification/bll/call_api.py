__author__ = 'Hai Bui'

import requests
import bll.config_log
import logging


def add_list_json_post(data):
    try:
        url = 'https://localhost:44347/api/Home/AddNewPost'
        # url = 'http://kltn26.somee.com/api/Home/AddNewPost'
        logging.info('Call to api ' + url)
        response = requests.post(url, json=data, verify=False)
        print('Status code: ', response.status_code)
        logging.info('Status code: ' + str(response.status_code))
        logging.info('Call api successfully')
        print(response.text)
        if response.text == 'true':
            return 0
        else:
            return -4
    except:
        logging.error('Call api failed')
        return -2


def get_all_black_list():
    try:
        url = 'https://localhost:44347/api/Home/GetAllBlackList'
        # url = 'http://kltn26.somee.com/api/Home/GetAllBlackList'
        logging.info('Call to api ' + url)
        response = requests.get(url, verify=False)
        print('Status code: ', response.status_code)
        logging.info('Status code: ' + str(response.status_code))
        logging.info('Call api successfully')
        return response.json()
    except:
        logging.error('Call api failed')
        return -2
