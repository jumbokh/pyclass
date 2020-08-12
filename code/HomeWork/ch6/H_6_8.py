S = 60000 #S表示一段期間存貨之總需求量
O = 120 #O表示每次訂購之訂購成本
C = 10 #C表示某段期間每單位存貨的儲存成本
def Q_function(x,y,z):
    Q = ((2*x*y)/z)**(1/2) #Q表示每批經濟訂購單數量
    return(Q)
print('訂購量為: %d 單位' %(Q_function(S,O,C)))
