# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:01:08 2015

@author: user
"""
target=3000000
rate=0.12
pv=10000
fv=0
n=0
while fv<target:
    fv=(fv+pv)*(1+rate/12)
    n=n+1
print('%s %d, %s %.2f' %('The totally saving is ', fv, 'The totally years you need is ', n/12))
