# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:30:43 2015

@author: user
"""
cash=50
count=0
for i in range(0, 50, 10):
    for j in range(0, 50, 5):
        for k in range(0, 50, 1):
            change=i+j+k
            if change==cash:
                count=count+1
print(count)
