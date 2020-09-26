class Money:
    def setValue(self,amount): #第一種方法
        self.amount =amount
    def showValue(self): #第二種方法
        print("錢的總數為:",self.amount)
s1 = Money()#第一個物件
s1.setValue("參萬捌仟元整")#呼叫方法時傳入字串
s1.showValue()
s2 = Money()#第二個物件
s2.setValue(34500)#呼叫方法時傳入浮點數值
s2.showValue()
