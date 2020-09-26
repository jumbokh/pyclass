print(__name__)

def SplitBill(bill,split):
    '''
    函數功能：分帳
    bill:帳單金額
    split:人數
    '''
    tip = 0.1  #10%服務費
    total = bill + (bill * tip)
    each_total = total / split
    each_pay = round(each_total, 0)
    return each_pay

def EvenTest(n): 
    '''
    函數功能：判斷奇偶數
    n:整數
    '''
    if (int(n) % 2) :
        return "奇數"
    else :
        return "偶數"