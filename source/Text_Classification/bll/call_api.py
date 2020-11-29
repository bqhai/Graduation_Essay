__author__ = 'Hai Bui'

import requests


def add_list_json_post(data):
    try:
        url = 'https://localhost:44347/api/Home/AddNewPost'
        response = requests.post(url, json=data, verify=False)
        print('Status code: ', response.status_code)
        print(response.text)
        return 0
    except:
        return -2


def get_all_black_list():
    try:
        url = 'https://localhost:44347/api/Home/GetAllBlackList'
        response = requests.get(url, verify=False)
        print('Status code: ', response.status_code)
        return response.json()
    except:
        return -2
