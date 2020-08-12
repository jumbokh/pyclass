# -*- coding: utf-8 -*-

lis1=list(range(5,20,1))
lis2=list(range(9,24,1))
lis1.append(sum(lis1))
lis2.append(sum(lis2))
a=(max(lis1)*max(lis2))-min(lis1)
lis2.clear()
lis2.append(a)
print(lis2)