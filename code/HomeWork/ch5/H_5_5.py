# H_5_5.py 功能:輸入頭和腳的數量，並判斷出有多少馴鹿及聖誕老人
# 輸入頭及腳的數量
head = int(input('請輸入頭的數量 : '))
foot = int(input('請輸入腳的數量 : '))
# 計算馴鹿和聖誕老人的數量
reindeer = (foot/2) - head
Santa = head - reindeer
# 將結果顯示出來
print('聖誕老人有 : %d 位' %(Santa))
print('馴鹿有 : %d 隻' %(reindeer))