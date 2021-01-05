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


def get_fb_id(url):
    split_url = url.split('fbid=')[1]
    split_url = split_url.split('&')[0]
    return split_url


def get_user_id(url):
    split_url = url.split('&id=')[1]
    split_url = split_url.split('&')[0]
    return split_url


def convert_intractive(input_str):
    if input_str.find('K') != -1:
        input_str = input_str.replace('K', '')
        if input_str.find('.') != -1:
            input_str = input_str.replace('.', '')
            input_str = int(input_str[0]) * 1000 + int(input_str[1]) * 100
        else:
            input_str = int(input_str) * 1000
    elif len(input_str) <= 0:
        input_str = 0
    else:
        # convert like to int if like < 1000
        input_str = int(input_str)
    return input_str


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
    facebook_id = url.split('/')[3]
    load_page.start(url.replace('www', 'm'), scroll_down, username, password)
    driver = load_page.driver
    global total_post_crawled
    list_json_post = []
    list_html_post = driver.find_elements_by_css_selector('[class="_55wo _5rgr _5gh8 async_like _1tl-"]')
    # page does not exit
    if len(list_html_post) == 0:
        logging.error('Page does not exit')
    print('Start crawling', len(list_html_post), 'posts...')
    logging.info('Start crawling ' + str(len(list_html_post)) + ' posts')
    for post in list_html_post:
        base_post_url = get_child_attribute(post, '[class="_52jc _5qc4 _78cz _24u0 _36xo"] a', 'href')
        post_url = 'https://www.facebook.com/' + get_fb_id(base_post_url) + '/'
        user_url = 'https://www.facebook.com/' + get_user_id(base_post_url) + '/'
        time = get_child_attribute(post, '[class="_52jc _5qc4 _78cz _24u0 _36xo"] a abbr', 'innerText')
        post_text = get_child_attribute(post, '[class="_5rgt _5nk5 _5msi"]', 'textContent')
        total_react = get_child_attribute(post, '[class="_1g06"]', 'innerText')
        total_cmts_and_shares = get_child_attribute(post, '[class="_1fnt"]', 'innerText')
        # Get like
        if total_react:
            if 'others' in total_react:
                total_react = convert_intractive(total_react.split(' ')[-2])
            else:
                total_react = convert_intractive(total_react)
        else:
            total_react = 0
        # Get comment & share
        if total_cmts_and_shares:
            cmt_flag = False
            sh_flag = False
            if total_cmts_and_shares.find('Comment') != -1:
                total_cmts_and_shares = total_cmts_and_shares.replace('Comment', '')
                total_cmts_and_shares = total_cmts_and_shares.replace('s', '')
                cmt_flag = True
            if total_cmts_and_shares.find('Share'):
                total_cmts_and_shares = total_cmts_and_shares.replace('Share', '')
                total_cmts_and_shares = total_cmts_and_shares.replace('s', '')
                sh_flag = True

            if cmt_flag and sh_flag:
                total_cmts = convert_intractive(total_cmts_and_shares.split(' ')[0])
                total_shares = convert_intractive(total_cmts_and_shares.split(' ')[1])
            elif not cmt_flag and sh_flag:
                total_cmts = 0
                total_shares = convert_intractive(total_cmts_and_shares.split(' ')[0])
            elif cmt_flag and not sh_flag:
                total_cmts = convert_intractive(total_cmts_and_shares.split(' ')[0])
                total_shares = 0
        else:
            total_cmts = 0
            total_shares = 0

        # Try to extract from the abbr element
        if time is not None:
            date = utils.parse_datetime(time, search=False)
            if date:
                time = date
            logger.debug("Could not parse date: %s", time)
        else:
            logger.warning("Could not find the abbr element for the date")

        list_json_post.append({
            'PostUrl': post_url,
            'UserUrl': user_url,
            'UploadTime': str(time),
            'CrawledTime': (datetime.now()).strftime("%Y/%m/%d %H:%M:%S"),
            'PostContent': post_text,
            # 'Image': image,
            'TotalLikes': total_react,
            'TotalComment': total_cmts,
            'TotalShare': total_shares,
            'FacebookID': facebook_id,
            'NewsLabelID': convert_label_to_text(predict(post_text))[0],
            'SentimentLabelID': convert_label_to_text(predict(post_text))[2]
        })
        total_post_crawled += 1
    if not list_json_post:
        logging.info('Nothing crawled')
        return -1
    else:
        # load_page.stop_and_save('data/facebook_user_post_crawled.json', list_json_post)
        logging.info('Finished crawling ' + str(total_post_crawled) + ' posts')
        return add_list_json_post(list_json_post)


def crawl(url, scroll_down, selection, username, password):
    if selection == 1:
        logging.info('Selection = Page ' + 'Scroll down = ' + str(scroll_down))
        return crawl_page(url, scroll_down * 6)
    elif selection == 2:
        logging.info('Selection = Group ' + 'Scroll down = ' + str(scroll_down))
        return crawl_group(url, scroll_down)
    elif selection == 3:
        logging.info('Selection = User ' + 'Scroll down = ' + str(scroll_down))
        return crawl_user(url, scroll_down, username, password)
