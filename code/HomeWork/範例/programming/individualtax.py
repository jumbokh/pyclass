# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:45:43 2015

@author: pckolin
"""
net=int(input('Please input the individual net income tax: '))
tax=0;
level2=520000*0.05
level3=level2+((1170000-520000)*0.13)
level4=level3+((2350000-1170000)*0.2)
level5=level4+((4400000-2350000)*0.3)
if net<=520000:
    tax=net*0.05
elif net<=1170000:
    tax=level2+((net-520000)*0.13)
elif net<=2350000:
    tax=level3+((net-1170000)*0.2)
elif net<=4400000:
    tax=level4+((net-2350000)*0.3)
elif net <10000000:
    tax=level5+((net-4400000)*0.4)
else:
    tax=level5+((net-10000000)*0.45)
print('%s=%.2f' %('The totally your indiviual tax due to pay', tax))

        