__author__ = 'Hai Bui'

from bll.common import *
import requests
import bll.config_log
import logging


def add_list_json_post(data):
    try:
        url = BASE_HOSTED_URL + 'api/Home/AddNewOrUpdateListPost/'
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


def check_exist_post(data):
    try:
        url = BASE_HOSTED_URL + 'api/Home/CheckExistPost/'
        logging.info('Call to api ' + url)
        response = requests.get(url, json=data,  verify=False)
        print('Status code: ', response.status_code)
        logging.info('Status code: ' + str(response.status_code))
        logging.info('Call api successfully')
        return response.json()
    except:
        logging.error('Call api failed')
        return -2


def add_json_post(data):
    try:
        url = BASE_HOSTED_URL + 'api/Home/AddNewPost/'
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


def update_json_post(data):
    try:
        url = BASE_HOSTED_URL + 'api/Home/UpdatePost/'
        logging.info('Call to api ' + url)
        response = requests.put(url, json=data, verify=False)
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


def get_all_watch_list():
    try:
        url = BASE_HOSTED_URL + 'api/Home/GetAllWatchList/'
        logging.info('Call to api ' + url)
        response = requests.get(url, verify=False)
        print('Status code: ', response.status_code)
        logging.info('Status code: ' + str(response.status_code))
        logging.info('Call api successfully')
        return response.json()
    except:
        logging.error('Call api failed')
        return -2


def check_exist_in_watch_list(facebook_id):
    try:
        url = BASE_HOSTED_URL + 'api/Home/CheckExistInWatchList/' + facebook_id + '/'
        logging.info('Call to api ' + url)
        response = requests.get(url, verify=False)
        print('Status code: ', response.status_code)
        logging.info('Status code: ' + str(response.status_code))
        logging.info('Call api successfully')
        return response.json()
    except:
        logging.error('Call api failed')
        return -2


def add_to_watch_list(watch_list):
    try:
        url = BASE_HOSTED_URL + 'api/Home/AddToWatchList/'
        logging.info('Call to api ' + url)
        response = requests.post(url, json=watch_list, verify=False)
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
