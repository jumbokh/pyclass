# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:27:36 2015

@author: user
"""
n=int(input('Please input n : '))
result=0
for i in range(2,n+1,1):
    result=result+(1-(1/i))
print('%s %.2f' %('The result is ', result))
