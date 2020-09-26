def SplitBill(bill,split):
    '''
    函數功能：分帳
    bill:帳單金額
    split:人數
    '''
    print(__name__)   #輸出__name__設定值
    
    tip = 0.1  #10%服務費
    total = bill + (bill * tip)
    each_total = total / split
    each_pay = round(each_total, 0)
    return each_pay

if __name__ == '__main__':    #判斷__name__
    pay = SplitBill(5000,3)
    print(pay)