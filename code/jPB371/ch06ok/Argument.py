def passFun(name, score):
    name = 'Michael'
    print('函數內部修改過的名字及分數')
    print('======================')
    print('名字:', name)
    #新增一個成績分數，會同步更動函數的的串列值
    score.append(85)
    print('分數:', score)

name1 = 'Andy'  #未呼叫函數前的名字設定值
score1 = [56, 84, 63] #未呼叫函數前的成績分數串列
print('函數呼叫前預設的名字及分數')
print('名字:', name1)
print('分數:', score1)
passFun(name1, score1)

print('函數內部被修改過回傳的名字及分數')
print('各位可以注意到名字沒變,但分數被修改了')
print('名字:', name1)
print('分數:', score1)
