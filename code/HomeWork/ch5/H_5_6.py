# H_5_6.py 功能:輸入金額後，判斷水果有幾種不同的買法
N = int(input('請輸入金額 : '))
if N >= 100 and N <= 1000: # 判斷金額是否有輸入錯誤
    for x in range(5,N//5,5): # N//5的部分是如果全部金額都買這項水果的最大值，當成是迴圈的末端
        for y in range(3,N//6,3):
            for z in range(2,N//10,2):
                if (x*5) + (y*6) + (z*10) == N :
                    print('x = %d  y = %d  z = %d' %(x,y,z))
                    d = x #將最後一組的組合儲存起來，方便後續判斷是否沒有解
                    e = y
                    f = z
else:
    print('輸入金額必須介在100~1000之間')
# 判斷如果沒有組合時，輸出 No Solution
if  N - ((d*5) + (e*6) + (f*10)) != 0 and N >= 100 and N <= 1000: 
    print('No Solution')
    