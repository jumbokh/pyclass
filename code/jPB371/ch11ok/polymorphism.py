#定義多形
class Product(): #父類別
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def profit(self):
        return self.price
    
    def show(self):
        return self.name
    
class Book(Product):#子類別
    def profit(self):        
        return self.price * 1.2
    
class Software(Product): #子類別
    def profit(self):
        return self.price *1.5

obj1 = Product('一般商品', 20000) #父類別物件
print('{:8s} 利潤 {:,}'.format(obj1.show(), obj1.profit()))

obj2 = Book('百科全書', 48000) #子類別物件
print('{:8s} 利潤 {:,}'.format(obj2.show(), obj2.profit()))

obj3 = Software('電腦軟體', 120000) #子類別物件
print('{:8s} 利潤 {:,}'.format(obj3.show(), obj3.profit()))
