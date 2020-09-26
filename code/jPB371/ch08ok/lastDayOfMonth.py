# -*- coding: utf-8 -*-

import datetime

def lastDayOfMonth(y,m):    
    d=datetime.date(y,m,1)
    yy = d.year
    mm = d.month
    
    if mm == 12 :
        mm = 1
        yy += 1
    else:
        mm += 1   
        
    return datetime.date(yy,mm,1)+ datetime.timedelta(days=-1)
    

if __name__ == '__main__':
    isYear=int(input("請輸入年："))
    isMonth=int(input("請輸入月："))
    lastDay=lastDayOfMonth(isYear,isMonth)
    print(lastDay)