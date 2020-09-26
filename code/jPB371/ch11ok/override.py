#子類別覆寫父類別的方法
class Discount(): #父類別
    def rate(self, total):
        self.price = total
        if self.price >= 20000:
            print('平日假日的折扣為9折：', end = ' ')
            return total * 0.9
        
class Festival(Discount): #子類別
    def rate(self, total): #覆寫rate方法
        self.price = total
        if self.price >= 50000:  
            print('節慶特優惠折扣為5折：', end = ' ')
            return total * 0.5

Jane = Discount()#建立父類別物件
print(Jane.rate(78000))

Mary = Festival()#建立子類別物件
print(Mary.rate(78000))
