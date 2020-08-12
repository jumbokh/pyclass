# RC_5_3功能: 簡化版個人綜合所得稅試算。
level1=520000*0.05
level2=(1170000-520000)*0.12
level3=(2350000-1170000)*0.2
level4=(4400000-2350000)*0.3
level5=(10000000-4400000)*0.4
try:
    income=input('請輸入淨年所得額:')
    # strip()可以去除字串裡的關鍵字  isdigit()如果字串裡都為數字返回True。否，則回傳False 
    if income.strip('-').isdigit()==False:            
        raise TypeError('非數字的字串')     #用raise自行發生例外處理   
    elif int(income)<0:
        raise ValueError('負值錯誤') 
    else:
        income=int(income)
        if income<=520000: #條件1
            tax=income*0.05
        elif income<=1170000: #條件2
            tax=level1+((income-520000)*0.12)
        elif income<=2350000: #條件3
            tax=level1+level2+((income-1170000)*0.2)
        elif income<=4400000: #條件4
            tax=level1+level2+level3+((income-2350000)*0.3)
        elif income<=10000000: #條件5
            tax=level1+level2+level3+level4+((income-4400000)*0.4)
        else: #條件6
            tax=level1+level2+level3+level4+level5+((income-10000000)*0.45)
        print('應繳稅額 =',tax)
except TypeError as v:
    print('型態錯誤，%s' %str(v))
except ValueError as v:
    print('數值錯誤，%s' %str(v))