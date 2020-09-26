score = [] #建立list來存放成績
# for廻圈建立輸入成績的list
for item in range(5):
   data = int(input('分數%2d ' %(item + 1)))
   score += [data]
print('%5s %5s ' % ('index', 'score'))

#for廻圈讀取成績並輸出
for item in range(len(score)):
   print('%3d %4d'% (item, score[item]))

print('-'*12)
# 利用內建函式sum()來計算總分
print('總分', sum(score), ', 平均 = ', sum(score)/5)
score.sort(reverse = True) # 使用sort()方法由大而小排序
print('遞減排序：', score)
print('遞增排序：', sorted(score)) #使用BIF
