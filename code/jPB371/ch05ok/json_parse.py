# -*- coding: utf-8 -*-
"""
OpenData資料擷取與應用
JSON格式
"""
od_json="http://opendata2.epa.gov.tw/AQI.json"

import urllib.request as ur
with ur.urlopen(od_json) as response:
    s=response.read()

import json
data = json.loads(s)
csv_str=""
for i in range(0, len(data)):
    csv_str += "{},{},{},{},{}\n".\
                format(data[i]["SiteName"],\
                       data[i]["County"],data[i]["PM2.5"],\
                           data[i]["Status"],data[i]["PublishTime"])
    
print(csv_str)