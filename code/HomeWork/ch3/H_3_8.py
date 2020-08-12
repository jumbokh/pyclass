# -*- coding: utf-8 -*-

lis1=list(range(9,-1,-1))
lis1.remove(0)
lis1.remove(3)
lis2=(25,30,11)
lis1.extend(lis2)
lis1=sorted(lis1,reverse=True)

print(lis1)