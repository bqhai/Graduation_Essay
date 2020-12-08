__author__ = 'Hai Bui'

from bll import load_page
from bll.text_classification import predict, convert_label_to_labelID
from bll.preprocessor import text_preprocess
from bll.call_api import *
from facebook_scraper import *
import re
import bll.config_log
import logging
# global variable
total_post_crawled = 0


def get_child_attribute(element, selector, attr):
    try:
        element = element.find_element_by_css_selector(selector)
        return str(element.get_attribute(attr))
    except:
        return ''


def count_crawled_post():
    return total_post_crawled


def crawl_page():
    driver = load_page.driver
    list_json_post = []
    list_html_post = driver.find_elements_by_css_selector('[class="_427x"] .userContentWrapper')
    # page does not exit
    if len(list_html_post) == 0:
        logging.error('Page does not exit')
        return -1
    print('Start crawling', len(list_html_post), 'posts...')
    logging.info('Start crawling ' + str(len(list_html_post)) + ' posts')

    global total_post_crawled
    total_post_crawled = len(list_html_post)

    for post in list_html_post:
        post_url = get_child_attribute(post, '._5pcq', 'href').split('?')[0]
        post_id = re.findall('\d+', post_url)[-1]
        time = get_child_attribute(post, 'abbr', 'title')
        post_text = get_child_attribute(post, '.userContent', 'textContent')
        total_react = get_child_attribute(post, '[data-testid="UFI2ReactionsCount/root"] ._81hb', 'innerText')
        total_shares = get_child_attribute(post, '._3rwx', 'innerText')
        total_cmts = get_child_attribute(post, '._3hg-', 'innerText')
        facebook_id = post_url.split('/')[3]

        # get number of like
        if total_react.find('K') != -1:
            total_react = total_react.replace('K', '')
            if total_react.find(',') != -1:
                total_react = total_react.replace(',', '')
                total_react = int(total_react[0]) * 1000 + int(total_react[1]) * 100
            else:
                total_react = int(total_react) * 1000

        # convert like to int if like < 1000
        total_react = int(total_react)

        # get number of comment and shares
        temp = [int(word) for word in total_shares.split() if word.isdigit()]
        if len(temp) > 0:
            total_shares = temp[0]
        temp = [int(word) for word in total_cmts.split() if word.isdigit()]
        if len(temp) > 0:
            total_cmts = temp[0]

        list_json_post.append({
            'PostUrl': post_url,
            'UploadTime': time,
            'PostContent': post_text,
            'TotalLikes': total_react,
            'TotalComment': total_cmts,
            'TotalShare': total_shares,
            'FacebookID': facebook_id,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })

    # load_page.stop_and_save('../data/facebook_post_crawled.json', list_json_post)
    logging.info('Finished crawling ' + str(len(list_html_post)) + ' posts')
    # call api post data to db
    return add_list_json_post(list_json_post)


def crawl_group(url, scroll_down):
    facebook_id = url.split('/')[4]
    list_json_post = []
    global total_post_crawled
    total_post_crawled = 0
    for post in get_posts(group=facebook_id, pages=scroll_down, extra_info=True):
        if str(post['post_id']) == 'None':
            post_url = 'None'
        else:
            post_url = 'https://www.facebook.com/' + str(post['post_id'])
        time = str(post['time'])
        user_url = 'https://www.facebook.com/' + str(post['user_id'])
        post_text = str(post['text'])
        total_react = post['likes']
        total_shares = post['shares']
        total_cmts = post['comments']

        list_json_post.append({
            'PostUrl': post_url,
            'UserUrl': user_url,
            'UploadTime': time,
            'PostContent': post_text,
            'TotalLikes': total_react,
            'TotalComment': total_cmts,
            'TotalShare': total_shares,
            'FacebookID': facebook_id,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })
        total_post_crawled += 1

    # load_page.stop_and_save('../data/facebook_group_post_crawled.json', list_json_post)
    logging.info('Finished crawling ' + str(total_post_crawled) + ' posts')
    return add_list_json_post(list_json_post)


def crawl(url, scroll_down, selection):
    if selection == 1:
        logging.info('Selection = Page ' + 'Scroll down = ' + str(scroll_down))
        page_url = url + 'posts/'
        load_page.start(page_url, scroll_down, selection)
        status = crawl_page()
        return status
    elif selection == 2:
        status = crawl_group(url, scroll_down)
        return status
    else:
        return -3
