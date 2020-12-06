__author__ = 'Hai Bui'

from facebook_scraper import *
from bll import load_page

# posts = list(get_posts(group='nhabaocongdan', pages=2, extra_info=True))
# print(posts)

# list_json_post = []
# for post in get_posts(group='nhabaocongdan', pages=1, extra_info=True):
#     post_url = 'https://www.facebook.com/' + str(post['post_id'])
#     time = str(post['time'])
#     user_id = 'https://www.facebook.com/' + str(post['user_id'])
#     post_text = post['text']
#     total_react = post['likes']
#     total_shares = post['shares']
#     total_cmts = post['comments']
#
#     list_json_post.append({
#         'PostUrl': post_url,
#         'Time': time,
#         'User': user_id,
#         'PostContent': post_text,
#         'TotalLikes': total_react,
#         'TotalComment': total_cmts,
#         'TotalShare': total_shares,
#     })
#
# load_page.stop_and_save('../data/facebook_group_post_crawled.json', list_json_post)

# for post in get_posts('viettan', pages=2, extra_info=True):
#     print(post)

for post in get_posts(group='nhabaocongdan', pages=2, extra_info=True):
    print(post)

