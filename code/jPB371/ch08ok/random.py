# -*- coding: utf-8 -*-

import random

print( random.random() ) 
print( random.uniform(1, 10) ) 
print( random.randint(1, 10) ) 
print( random.randrange(0, 50, 5) ) 
print( random.choice(["真真", "小宇", "大凌"]) ) 

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print( items )

print( random.sample('ABCDEFG', 2) )
