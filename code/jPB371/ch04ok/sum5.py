# -*- coding: utf-8 -*-
"""
某一個數字範圍內5的倍數進行加總
"""
sum = 0 #儲存加總結果

# 進入for/in迴圈
for count in range(0, 21, 5):
    sum += count #將數值累加      

print('5的倍數累加結果=',sum) #輸出累加結果
