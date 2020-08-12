# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:45:19 2015

@author: user
"""
temp=[0]
import random as rd
for i in range(1, 11,1):
    for j in range(1,11,1):
        temp=rd.randint(0,10)
        str='%2d ' %(temp)
        print(str, end='')        
    print('\n')

