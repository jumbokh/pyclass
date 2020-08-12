# H_5_3.py 功能:輸入兩個陣列，並且完成加減乘除後輸出顯示
# 儲存在A的陣列
matrix1_1 = []
matrix1_2 = []
matrix1_3 = []
# 儲存在B的陣列
matrix2_1 = []
matrix2_2 = []
matrix2_3 = []
# 存放相加後的陣列
matrix3_1 = []
matrix3_2 = []
matrix3_3 = []
# 存放相減後的陣列
matrix4_1 = []
matrix4_2 = []
matrix4_3 = []
# 存放相乘後的陣列
matrix5_1 = []
matrix5_2 = []
matrix5_3 = []
# 存放相除後的陣列
matrix6_1 = []
matrix6_2 = []
matrix6_3 = []
# 陣列A輸入
for r in range(0,3,1):
    n = int(input('請輸入A陣列的(0,%d) : ' %(r)))
    matrix1_1.insert(r,n)
for r in range(0,3,1):
    n = int(input('請輸入A陣列的(1,%d) : ' %(r)))
    matrix1_2.insert(r,n)
for r in range(0,3,1):
    n = int(input('請輸入A陣列的(2,%d) : ' %(r)))
    matrix1_3.insert(r,n)
# 陣列B輸入
for r in range(0,3,1):
    n = int(input('請輸入B陣列的(0,%d) : ' %(r)))
    matrix2_1.insert(r,n)
for r in range(0,3,1):
    n = int(input('請輸入B陣列的(1,%d) : ' %(r)))
    matrix2_2.insert(r,n)
for r in range(0,3,1):
    n = int(input('請輸入B陣列的(2,%d) : ' %(r)))
    matrix2_3.insert(r,n)
# 計算相加的迴圈
for r in range(0,3,1):
    matrix3_1.insert(r,matrix1_1[r] + matrix2_1[r])
    matrix3_2.insert(r,matrix1_2[r] + matrix2_2[r])
    matrix3_3.insert(r,matrix1_3[r] + matrix2_3[r])
print('-----分隔線-----')
print(matrix3_1)
print(matrix3_2)
print(matrix3_3)  
# 計算相減的迴圈
for r in range(0,3,1):
    matrix4_1.insert(r,matrix1_1[r] - matrix2_1[r])
    matrix4_2.insert(r,matrix1_2[r] - matrix2_2[r])
    matrix4_3.insert(r,matrix1_3[r] - matrix2_3[r])
print('-----分隔線-----')
print(matrix4_1)
print(matrix4_2)
print(matrix4_3)  
# 計算相乘的迴圈
for r in range(0,3,1):
    matrix5_1.insert(r,matrix1_1[r] * matrix2_1[r])
    matrix5_2.insert(r,matrix1_2[r] * matrix2_2[r])
    matrix5_3.insert(r,matrix1_3[r] * matrix2_3[r])
print('-----分隔線-----')
print(matrix5_1)
print(matrix5_2)
print(matrix5_3)  
# 計算相除的迴圈
for r in range(0,3,1):
    matrix6_1.insert(r,round(matrix1_1[r] / matrix2_1[r],2))
    matrix6_2.insert(r,round(matrix1_2[r] / matrix2_2[r],2))
    matrix6_3.insert(r,round(matrix1_3[r] / matrix2_3[r],2))  
print('-----分隔線-----')
print(matrix6_1)
print(matrix6_2)
print(matrix6_3)