# H_5_4.py 功能:輸入數字後判斷是否為11的倍數
num_even = 0 # 儲存偶數位數字暫存
num_odd = 0 # 儲存奇數位數字暫存

number = str(input('請輸入數字 : '))
l = len(number) # 判斷輸入數字之長度
x = int(number) # 轉換成數值型態

for n in range(l,0,-1):
    y = x//(10**(n-1)) # 計算奇偶位數字
    x = x - (y*(10**(n-1)))
    if n%2 == 0: # 判斷若是偶數位數字則儲存在偶數位暫存，反之存奇數位暫存
        num_even = num_even + y
    else:
        num_odd = num_odd + y
# 判斷是否為11的倍數
if abs(num_even - num_odd) == 0 or (abs(num_even - num_odd))%11 == 0:
    print('此數為11的倍數')
else:
    print('此數不是11的倍數')