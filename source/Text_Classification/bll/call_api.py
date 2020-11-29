__author__ = 'Hai Bui'

import requests


def add_list_json_post(data):
    url = 'https://localhost:44347/api/Home/AddNewPost'
    response = requests.post(url, json=data, verify=False)
    print('Status code: ', response.status_code)
    print(response.text)

