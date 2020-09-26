# -*- coding: utf-8 -*-
"""
使用Facebook API蒐集粉絲專頁PO文
JSON格式
"""

import urllib.request as ur

access_token="EAACEdEose0cBAOr9JdbNwSpBGdOeKgZCuWn24wXsqr3xnZA1taleuSRJW7UnSr3qt0mxBTkgjI6t4Cna2H7sXyOA9mZAyZAGv77NkZAxmf0WrbhfZCZBIkRBZATv6AE5rTUtsEgfpdY2f2hDUc9hb0iG1OTPY8rT1Vxhg24cvPnwBUruWletfw0zDZA8ZBGOO7N7IZD"
access_id="368113116692686"

urls = "https://graph.facebook.com/v2.11/{}/posts?limit=2&access_token={}".format(access_id,access_token)

with ur.urlopen(urls) as response:
    s=response.read()

import json
r = json.loads(s)
r_data=r['data']

for i in range(len(r_data)):
    print("{0}\n{1}\n".format(r_data[i]["created_time"],r_data[i]["message"]))
