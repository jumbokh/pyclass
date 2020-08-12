# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:34:23 2016

@author: cat
"""

lis1=list(range(28,53,3))

print("最大值%d，最小值%d，總和%d"%(max(lis1),min(lis1),abs(min(lis1)-(sum(lis1)/len(lis1)))))