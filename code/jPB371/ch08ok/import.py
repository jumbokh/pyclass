# -*- coding: utf-8 -*-

import random

a = random.randint(0,99)  #使用randint函數隨機取得整數
print(a)

items = [1, 2, 3, 4, 5]
random.shuffle(items)  #使用shuffle函數將數列洗牌
print(items)
