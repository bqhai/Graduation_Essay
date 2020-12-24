# __author__ = 'Hai Bui'
#
# from helium import *
# import json
# import time
# import bll.config_log
# import logging
#
#
# def load_more_posts():
#     time.sleep(1)
#     js_script = 'window.scrollTo(0, document.body.scrollHeight)'
#     driver.execute_script(js_script)
#     while find_all(S('.async_saving [role="progressbar"]')):
#         pass
#
#
# def start(url='', scroll_down=0, selection=0, login_option=False, username='', password=''):
#     global driver
#     print('Go to page', url)
#     logging.info('Go to page ' + url)
#     driver = start_chrome(url, headless=False)
#
#     # start for FB page
#     if selection == 1:
#         # wait_until(Text('Không thể xử lý yêu cầu của bạn').exists)
#         btn_close = find_all(S('[class="autofocus _9l2h  layerCancel _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]'))
#         if btn_close:
#             print('Click Close button')
#             click(btn_close[0])
#             logging.info('Click Close button at page')
#
#         print('Load more posts and check for Not Now button')
#         load_more_posts()
#         logging.info('Load more posts and check for Not Now button')
#         btn_notnow = find_all(S('#expanding_cta_close_button'))
#         if btn_notnow:
#             print('Click Not Now button')
#             click(btn_notnow[0].web_element.text)
#
#     # start for FB group
#     # if selection == 2:
#     #     btn_close = find_all(S(
#     #         '[class="oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329"]'))
#     #     if btn_close:
#     #         print('Click Close button')
#     #         click(btn_close[0])
#     #     if login_option:
#     #         write(username, into='Email hoặc điện thoại')
#     #         write(password, into='Mật Khẩu')
#     #         click('Accessible login button')
#     for i in range(scroll_down):
#         btn_close = find_all(S('[class="autofocus _9l2h  layerCancel _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]'))
#         if btn_close:
#             print('Click Close button')
#             click(btn_close[0])
#             logging.info('Click Close button at page')
#         print('Load more posts times', i + 1, '/', scroll_down)
#         load_more_posts()
#         logging.info('Load more posts times ' + str(i + 1) + '/' + str(scroll_down))
#
#
# # Save data crawled to json
# def stop_and_save(file_name, list_posts):
#     print('Save crawled data...')
#     with open(file_name, 'w', encoding='utf-8') as file:
#         json.dump(list_posts, file, ensure_ascii=False, indent=4)
# # kill_browser()
