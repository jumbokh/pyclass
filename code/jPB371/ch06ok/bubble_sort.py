# -*- coding: utf-8 -*-
'''
氣泡排序法
'''

def bubble_sort(L):
    N = len(L)
    cc=0
    x=0
    for i in range(N-1):       
        for j in range(1, N - i):  #從1比較到倒數n-i
            x+=1
            print("{},{}".format(L[j - 1],L[j]))
            if L[j - 1] > L[j]:                
                L[j - 1], L[j] = L[j], L[j - 1]
        cc+=1
        print("第{}次排序結果：{}".format(cc,L))
    return L,x


a = [10, 3, 12, 20, 16]  #排序的資料
print("排序前: {}".format(a))
L,x = bubble_sort(a)
print("排序後: {}".format(L))
print("比較次數：{}".format(x))
