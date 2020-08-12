# -*- coding: utf-8 -*-

lis1=list(range(5,20,1))
lis2=list(range(9,24,1))
lis1.append(sum(lis1))
lis2.append(sum(lis2))
lis1=sorted(lis1,reverse=True)
lis2=sorted(lis2,reverse=True)
print(lis1.pop()*lis2.pop())