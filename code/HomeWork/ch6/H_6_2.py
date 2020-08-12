def magic(n):
	square = []
	for i in range(n + 1):
		square.append([0] * (n + 1))
	i = 0
	j = (n + 1) // 2
	for key in range(1, n ** 2 + 1):
		if key % n == 1:
			i += 1
		else:
			i -= 1
			j += 1
		if i == 0:
			i = n
		if j > n:
			j = 1
		square[i][j] = key
	matrix = []
	
	for i in range(n):
		matrix.append([0] * n)
	for k in range(len(matrix)):
		for l in range(len(matrix[0])):
			matrix[k][l] = square[k + 1][l + 1]
	return matrix

#給予初始數值
num = eval(input("請輸入階數n(不得大於10的奇數，輸入0則結束程式)："))

#若num不等於0，則程序會一直執行
while num != 0:
	#驗證條件
	if num > 0 and num <= 10 and num % 2 == 1:
		matrix = magic(num)
		for i in matrix:
			print(i)
	else:
		print("請輸入正確的數值")
	#輸入下一個數值
	num = eval(input("請輸入階數n(不得大於10，輸入0則結束程式)："))

