# -*- coding: utf-8 -*-
"""
樂透開獎與對獎程式
題目要求：
1.讓投注者輸入5個不重複的號碼，每個號碼以逗號(,)隔開
2.隨機產生開獎號碼。
3.計算投注者的5個號碼有幾個號碼開出。
4.輸出需包含開獎號碼的開出順序、大小順序，投注者選的號碼以及符合的號碼；
如果沒有符合則顯示「沒有符合!」。
"""

import random

def generate_num():    
    auto_num = []
    while len(auto_num)<6:
        x = random.randint(1, 50)
        if x not in auto_num:
            auto_num.append(x)   
    return auto_num

def lottoCheck(a):
    b=generate_num()
    b_sort=sorted(b)
    print("開出順序：{}".format(b))
    print("大小順序：{}".format(b_sort))    
    print("您選的號碼：{}".format(sorted(a)))
    ans = set(a) & set(b_sort)
    if len(ans):
        print("符合：{}".format(ans))
    else:
        print("沒有符合!")
        

    
if __name__ == "__main__": 
    while True:
        try:
            user_number = input("請從1~39個號碼任選5個不同號碼，每個號碼請以逗號(,)隔開：")
            
            if user_number.count(",")<4:
                print("號碼不足，",end="")
                raise ValueError
            else:
                n1=[]
                for n in user_number.split(","):    
                    n = int(n)
                    if n in n1:
                        print("重複輸入，",end="")
                        raise ValueError
                    elif n not in range(1,40):
                        print("超出範圍!數字必須是1~39，",end="")
                        raise ValueError
                    else:
                        n1.append(n)                            
                lottoCheck(n1)                
                break
        except ValueError:
            print("請再輸入一次!")