__author__ = 'Hai Bui'

from bll import load_page
import re
import requests
from bll.text_classification import predict, convert_label_to_labelID
from bll.preprocessor import text_preprocess
from bll.call_api import *

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
    print('Start crawling', len(list_html_post), 'posts...')

    # page does not exit
    if len(list_html_post) == 0:
        return -1

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
            'PostID': post_id,
            'Time': time,
            'PostContent': post_text,
            'TotalLikes': total_react,
            'TotalComment': total_cmts,
            'TotalShare': total_shares,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })

    load_page.stop_and_save('../data/facebook_post_crawled.json', list_json_post)

    # call api post data to db
    return add_list_json_post(list_json_post)


def crawl_group():
    driver = load_page.driver
    list_json_post = []
    list_html_post = driver.find_elements_by_css_selector('[class="j83agx80 l9j0dhe7 k4urcfbm"]')
    print('Start crawling', len(list_html_post), 'posts...')

    for post in list_html_post:
        post_url = get_child_attribute(post,
                                       '[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl py34i1dx gpro0wi8"]',
                                       'href').split('?')[0]
        # post_id = re.findall('\d+', post_url)[-1]
        time = get_child_attribute(post,
                                   '[class="b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4"]',
                                   'textContent')

        # btn_show_more = find_all(S(
        #     '[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]'))
        # if btn_show_more:
        #     print('Click Show more button')
        #     click(btn_show_more[0].web_element.text)

        post_text = get_child_attribute(post,
                                        '[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m',
                                        'textContent')

        list_json_post.append({
            'PostUrl': post_url,
            'Time': time.replace('=', ''),
            'PostContent': post_text,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })

    load_page.stop_and_save('../data/facebook_group_post_crawled.json', list_json_post)


def crawl(url, scroll_down, selection):
    if selection == 1:
        page_url = url + 'posts/'
        load_page.start(page_url, scroll_down, selection)
        status = crawl_page()
        return status
    elif selection == 2:
        load_page.start(url, scroll_down, selection)
        crawl_group()
    else:
        print('Chức năng này hiện đang trong giai đoạn phát triển')
