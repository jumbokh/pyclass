with open('introduct.txt', 'rt') as foin:
    total = foin.readlines()#一次讀取所有行

#取得行數，再以for廻圈讀取
print('行數：', len(total))
for line in total:
    print(line, end = '')
