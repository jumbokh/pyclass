# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:15:22 2015

@author: user
"""
salary=30000
expenditure=19000

age=25
future=28
salaryrate=0.03
exprate=0.02
salaryfv=salary
expfv=expenditure
savingfv=0
for i in range(age+1, future+1,1):
    salaryfv=salaryfv*(1+salaryrate)
    expfv=expfv*(1+exprate)
    savingfv=savingfv+((salaryfv-expfv)*12)
print('%s %d' %('The totally salary is', salaryfv))
print('%s %d' %('The totally expenditure is', expfv))
print('%s %d' %('The totally saving is', savingfv))