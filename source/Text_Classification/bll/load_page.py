from helium import *
import json


def load_more_posts():
    js_script = 'window.scrollTo(0, document.body.scrollHeight)'
    driver.execute_script(js_script)
    while find_all(S('.async_saving [role="progressbar"]')) != []: pass


def start(url='', scroll_down=0):
    global driver
    print('Go to page', url)
    driver = start_chrome(url, headless=False)

    print('Load more posts and check for Not Now button')
    # load_more_posts()

    btnClose = find_all(S('[class="autofocus  layerCancel _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]'))
    if btnClose != []:
        print('Click Close button')
        click(btnClose[0])

    btnNotNow = find_all(S('#expanding_cta_close_button'))
    if btnNotNow != []:
        print('Click Not Now button')
        click(btnNotNow[0].web_element.text)

    for i in range(scroll_down - 1):
        print('Load more posts times', i + 1, '/', scroll_down)
        load_more_posts()


def stop_and_save(fileName, listPosts):
    print('Save crawled data...')
    with open(fileName, 'w', encoding='utf-8') as file:
        json.dump(listPosts, file, ensure_ascii=False, indent=4)
# kill_browser()
