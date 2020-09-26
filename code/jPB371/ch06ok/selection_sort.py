# -*- coding: utf-8 -*-

def selectionSort(L):
    N = len(L)
    cc = 0
    x=0
    for i in range(N-1):
        minL = i
        for j in range(i+1, N):   #找出最小值
            x+=1
            if L[minL] > L[j]:
                minL = j
        
        # 把最小值跟第 i 個做交換
        L[minL], L[i] = L[i], L[minL]
        cc += 1
        print("第{}次排序結果：{}".format(cc,L))
    return L,x

a = [10, 3, 12, 20, 16]  #排序的資料
print("排序前: {}".format(a))
L,x = selectionSort(a)
print("排序後: {}".format(L))
print("比較次數：{}".format(x))
