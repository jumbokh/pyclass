# -*- coding: utf-8 -*-

import os
CF=os.getcwd()

CF_listdir=os.listdir( CF )

os.mkdir(CF+"/newFolder")  #建立資料夾
os.mkdir(CF+"/newFolder1")  #建立資料夾

os.rename(CF+"/newFolder1",CF+"/renewFolder") #更名

print("目前資料夾:"+CF)
print("資料夾裡的文件與資料夾:{}".format(CF_listdir))

