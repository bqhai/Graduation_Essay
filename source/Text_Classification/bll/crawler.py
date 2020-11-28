from bll import load_page
import re
import requests
from bll.text_classification import predict, convert_label_to_labelID
from bll.preprocessor import text_preprocess

POSTS = '/posts/'
PAGE_URL = 'https://www.facebook.com/vnesportstv' + POSTS
PAGE_ID = 'vnesportstv'
SCROLL_DOWN = 2


def get_child_attribute(element, selector, attr):
    try:
        element = element.find_element_by_css_selector(selector)
        return str(element.get_attribute(attr))
    except:
        return ''


def crawl_page():
    driver = load_page.driver
    list_json_posts = []
    list_html_posts = driver.find_elements_by_css_selector('[class="_427x"] .userContentWrapper')
    print('Start crawling', len(list_html_posts), 'posts...')

    for post in list_html_posts:
        post_url = get_child_attribute(post, '._5pcq', 'href').split('?')[0]
        post_id = re.findall('\d+', post_url)[-1]
        time = get_child_attribute(post, 'abbr', 'title')
        post_text = get_child_attribute(post, '.userContent', 'textContent')
        total_react = get_child_attribute(post, '[data-testid="UFI2ReactionsCount/root"] ._81hb', 'innerText')
        total_shares = get_child_attribute(post, '._3rwx', 'innerText')
        total_cmts = get_child_attribute(post, '._3hg-', 'innerText')

        # get number in like, comment and shares
        if total_react.find('K') != -1:
            total_react = total_react.replace('K', '')
            temp = [int(word) for word in total_react.split() if word.isdigit()]

        temp = [int(word) for word in total_shares.split() if word.isdigit()]
        if len(temp) > 0:
            total_shares = temp[0]
        temp = [int(word) for word in total_cmts.split() if word.isdigit()]
        if len(temp) > 0:
            total_cmts = temp[0]

        list_json_posts.append({
            'PostUrl': post_url,
            'PostID': post_id,
            'Time': time,
            'PostContent': post_text,
            'TotalLikes': total_react,
            'TotalComment': total_cmts,
            'TotalShare': total_shares,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })

    load_page.stop_and_save('../data/facebook_post_crawled.json', list_json_posts)

    # url = 'https://localhost:44347/api/Home/AddNewPost'
    # response = requests.post(url, json=list_json_posts, verify=False)
    # print('Status code: ', response.status_code)
    # print(response.text)


def crawl_group():
    driver = load_page.driver
    list_json_posts = []
    list_html_posts = driver.find_elements_by_css_selector('[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')
    print('Start crawling', len(list_html_posts), 'posts...')

    for post in list_html_posts:
        post_url = get_child_attribute(post, '[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]', 'href').split('?')[0]
        # post_id = re.findall('\d+', post_url)[-1]
        time = get_child_attribute(post, '[class="b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4"]', 'textContent')
        post_text = get_child_attribute(post, '[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m"]', 'textContent')

        list_json_posts.append({
            'PostUrl': post_url,
            'Time': time.replace('=', ''),
            'PostContent': post_text,
            'NewsLabelID': convert_label_to_labelID(predict(text_preprocess(post_text)))
        })

    load_page.stop_and_save('../data/facebook_group_post_crawled.json', list_json_posts)


def crawl(url, scroll_down, selection):
    if selection == 1:
        load_page.start(url, scroll_down, selection)
        crawl_page()
    elif selection == 2:
        load_page.start(url, scroll_down, selection)
        crawl_group()
    else:
        print('Đang cào trang cá nhân')
