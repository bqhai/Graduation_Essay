__author__ = 'Hai Bui'

from helium import *
import json
import time
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
    driver = start_chrome(url, headless=False)

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

    # print('Load more posts and check for Not Now button')
    # load_more_posts()
    # logging.info('Load more posts and check for Not Now button')
    # btn_notnow = find_all(S('#expanding_cta_close_button'))
    # if btn_notnow:
    #     print('Click Not Now button')
    #     click(btn_notnow[0].web_element.text)
    time.sleep(5)
    for i in range(scroll_down):
        print('Load more posts times', i + 1, '/', scroll_down)
        load_more_posts()
        logging.info('Load more posts times ' + str(i + 1) + '/' + str(scroll_down))


# Save data crawled to json
def stop_and_save(file_name, list_posts):
    print('Save crawled data...')
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(list_posts, file, ensure_ascii=False, indent=4)
# kill_browser()
