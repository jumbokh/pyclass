def function_calculate(n):
    result = 0
    for x in range(1,n+1,1):
        result += 1/(2**x)
    return(result)
n = int(input('請輸入n值:'))
print('輸出值為 : %f' %(function_calculate(n)))
