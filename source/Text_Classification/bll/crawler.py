__author__ = 'Hai Bui'

from bll.text_classification import predict, convert_label_to_text
from bll.call_api import *
from facebook_scraper import *
from bll import load_page
import re
import bll.config_log
from datetime import datetime
import logging

# global variable
total_post_crawled = 0
stop_flag = False


def set_stop_flag(state):
    global stop_flag
    stop_flag = state


def count_crawled_post():
    global total_post_crawled
    temp = total_post_crawled
    total_post_crawled = 0
    return temp


def get_child_attribute(element, selector, attr):
    try:
        element = element.find_element_by_css_selector(selector)
        return str(element.get_attribute(attr))
    except:
        return ''


def crawl_page(url, scroll_down):
    facebook_id = url.split('/')[3]
    list_json_post = []
    global total_post_crawled
    total_post_crawled = 0
    try:
        for post in get_posts(facebook_id, pages=scroll_down, extra_info=True):
            global stop_flag
            if stop_flag:
                break
            if str(post['post_id']) == 'None':
                post_url = None
            else:
                post_url = 'https://www.facebook.com/' + facebook_id + '/posts/' + str(post['post_id'])
            user_url = 'https://www.facebook.com/' + str(post['user_id'])
            time = str(post['time'])
            post_text = str(post['text'])
            image = str(post['image'])
            total_react = post['likes']
            total_shares = post['shares']
            total_cmts = post['comments']

            list_json_post.append({
                'PostUrl': post_url,
                'UserUrl': user_url,
                'UploadTime': time,
                'CrawledTime': (datetime.now()).strftime("%Y/%m/%d %H:%M:%S"),
                'PostContent': post_text,
                'Image': image,
                'TotalLikes': total_react,
                'TotalComment': total_cmts,
                'TotalShare': total_shares,
                'FacebookID': facebook_id,
                'NewsLabelID': convert_label_to_text(predict(post_text))[0],
                'SentimentLabelID': convert_label_to_text(predict(post_text))[2]
            })
            total_post_crawled += 1
    except:
        return -1
    if not list_json_post:
        logging.info('Page does not exits')
        return -1
    else:
        # load_page.stop_and_save('../data/facebook_post_crawled.json', list_json_post)
        logging.info('Finished crawling ' + str(total_post_crawled) + ' posts')
        return add_list_json_post(list_json_post)


def crawl_group(url, scroll_down):
    facebook_id = url.split('/')[4]
    list_json_post = []
    global total_post_crawled
    total_post_crawled = 0
    try:
        for post in get_posts(group=facebook_id, pages=scroll_down, extra_info=True):
            global stop_flag
            if stop_flag:
                break
            if str(post['post_id']) == 'None':
                post_url = None
            else:
                post_url = 'https://www.facebook.com/groups/' + facebook_id + '/permalink/' + str(post['post_id']) + '/'
            time = str(post['time'])
            user_url = 'https://www.facebook.com/' + str(post['user_id'])
            post_text = str(post['text'])
            image = str(post['image'])
            total_react = post['likes']
            total_shares = post['shares']
            total_cmts = post['comments']

            list_json_post.append({
                'PostUrl': post_url,
                'UserUrl': user_url,
                'UploadTime': time,
                'CrawledTime': (datetime.now()).strftime("%Y/%m/%d %H:%M:%S"),
                'PostContent': post_text,
                'Image': image,
                'TotalLikes': total_react,
                'TotalComment': total_cmts,
                'TotalShare': total_shares,
                'FacebookID': facebook_id,
                'NewsLabelID': convert_label_to_text(predict(post_text))[0],
                'SentimentLabelID': convert_label_to_text(predict(post_text))[2]
            })
            total_post_crawled += 1
    except:
        return -1
    if not list_json_post:
        logging.info('Group does not exits')
        return -1
    else:
        # load_page.stop_and_save('../data/facebook_group_post_crawled.json', list_json_post)
        logging.info('Finished crawling ' + str(total_post_crawled) + ' posts')
        return add_list_json_post(list_json_post)


def crawl_user(url, scroll_down, username, password):
    load_page.start(url, scroll_down, username, password)
    driver = load_page.driver


def crawl(url, scroll_down, selection, username, password):
    if selection == 1:
        logging.info('Selection = Page ' + 'Scroll down = ' + str(scroll_down))
        return crawl_page(url, scroll_down * 6)
    elif selection == 2:
        logging.info('Selection = Group ' + 'Scroll down = ' + str(scroll_down))
        return crawl_group(url, scroll_down)
    else:
        logging.info('Selection = User ' + 'Scroll down = ' + str(scroll_down))
        return crawl_user(url, scroll_down, username, password)
