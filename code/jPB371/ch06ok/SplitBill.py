# -*- coding: utf-8 -*-
'''
分帳程式
'''

def SplitBill():
    bill = float(input("帳單金額："))
    split = float(input("分帳人數："))
    tip = 0.1  #10%服務費
    total = bill + (bill * tip)
    each_total = total / split
    each_pay = round(each_total, 0)
    return each_total, each_pay
 

e1 ,e2 = SplitBill()
print("每人應付{},應付：{}".format(e1, e2))