# -*- coding: utf-8 -*-
'''
將串列中奇偶數分離
'''

Number = [1,2,3,4,5,6,7,8,9,10] 
even_num = Number[1::2]
odd_num = Number[0::2]
    
print("偶數：{}\n奇數：{}".format(even_num,odd_num))
