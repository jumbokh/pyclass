# H_5_9.py 功能:輸入西曆年，判斷是否為閏年
# 輸入西曆年
year = int(input('請輸入西曆年 : '))
# 判斷是否為閏年
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('%d 年是閏年' %(year)) # 判斷結果為閏年，顯示出來
else:
    print('%d 年不是閏年' %(year)) # 判斷結果不為閏年，顯示出來
