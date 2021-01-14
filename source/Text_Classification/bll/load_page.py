__author__ = 'Hai Bui'

from helium import *
import json
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bll.config_log
import logging


def load_more_posts():
    time.sleep(1)
    js_script = 'window.scrollTo(0, document.body.scrollHeight)'
    driver.execute_script(js_script)
    while find_all(S('.async_saving [role="progressbar"]')):
        pass


def start(url='', scroll_down=0, username='', password=''):
    global driver
    print('Go to page', url)
    logging.info('Go to page ' + url)
    option = Options()
    option.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    driver = start_chrome(url, headless=False, options=option)

    btn_login = find_all(S('[class="_54k8 _56bs _4n44 _6gg6 _901w _56bv _52jh"]'))
    if btn_login:
        click(btn_login[0])
        time.sleep(6)
        write(username, into='Số di động hoặc email')
        time.sleep(6)
        write(password, into='Mật Khẩu')
        time.sleep(6)
        btn_login_2 = find_all(S('[name="login"]'))
        click(btn_login_2[0])
    else:
        write(username, into='Số di động hoặc email')
        time.sleep(6)
        write(password, into='Mật Khẩu')
        time.sleep(6)
        btn_login_2 = find_all(S('[name="login"]'))
        click(btn_login_2[0])

    time.sleep(5)
    load_more_posts()
    for i in range(scroll_down):
        time.sleep(1)
        print('Load more posts times', i + 1, '/', scroll_down)
        load_more_posts()
        logging.info('Load more posts times ' + str(i + 1) + '/' + str(scroll_down))


# Save data crawled to json
def stop_and_save(file_name, list_posts):
    print('Save crawled data...')
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(list_posts, file, ensure_ascii=False, indent=4)


def stop():
    kill_browser()
