from bll import load_page
import re
import requests

POSTS = '/posts/'
PAGE_URL = 'https://www.facebook.com/viettan' + POSTS
PAGE_ID = 'viettan'
SCROLL_DOWN = 2


def get_child_attribute(element, selector, attr):
    try:
        element = element.find_element_by_css_selector(selector)
        return str(element.get_attribute(attr))
    except:
        return ''


load_page.start(PAGE_URL, SCROLL_DOWN)
driver = load_page.driver

listJsonPosts = []
listHtmlPosts = driver.find_elements_by_css_selector('[class="_427x"] .userContentWrapper')
print('Start crawling', len(listHtmlPosts), 'posts...')

for post in listHtmlPosts:
    post_url = get_child_attribute(post, '._5pcq', 'href').split('?')[0]
    post_id = re.findall('\d+', post_url)[-1]
    time = get_child_attribute(post, 'abbr', 'title')
    post_text = get_child_attribute(post, '.userContent', 'textContent')
    total_react = get_child_attribute(post, '[data-testid="UFI2ReactionsCount/root"] ._81hb', 'innerText')
    total_shares = get_child_attribute(post, '[data-testid="UFI2SharesCount/root"]', 'innerText')
    total_cmts = get_child_attribute(post, '._3hg-', 'innerText')

    # get number in comment and shares
    # total_cmts = [int(i) for i in total_cmts.split() if i.isdigit()]
    # total_shares = [int(i) for i in total_shares.split() if i.isdigit()]

    listJsonPosts.append({
        'PostUrl': post_url,
        'PostID': post_id,
        'Time': time,
        'PostContent': post_text,
        'TotalLikes': total_react,
        'TotalComment': total_cmts,
        'TotalShare': total_shares,
    })

load_page.stop_and_save(
    'D:\\ThucHanh\\GitHub\\Graduation_Essay\\source\\Text_Classification\\data\\facebook_post_crawled.json',
    listJsonPosts)

url = 'https://localhost:44347/api/Home/AddNewPost'
response = requests.post(url, json=listJsonPosts, verify=False)
print("Status code: ", response.status_code)
print(response.text)
