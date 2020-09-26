class Person:
    #定義方法一：取得姓名和年齡
    def setData(self, name, age):
        self.name = name
        self.age = age
    #定義方法二：輸出姓名和年齡
    def showData(self):
        print('姓名:{0:6s}, 年齡:{1:4s}'.format(
            self.name, self.age))
# 產生物件
boy1=Person()#物件1
boy1.setData('John', '16')
boy1.showData() #呼叫方法
boy2=Person()#物件2
boy2.setData('Andy', '14')
boy2.showData()
