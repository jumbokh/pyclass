a = [18, -51, 23, 35, 10, 9, -3, 52, 81, 69]
b = [28, 32, -35, 40, 73, 17, 92, 32, 13, 29]
def sum_function(n): 
    list_sum = 0
    for m in range(0,n+1,1):
        list_sum = list_sum + (a[m] * b[n-m])
    return(list_sum)
n = len(a) - 1
print('輸出值為 : %d' %(sum_function(n)))
