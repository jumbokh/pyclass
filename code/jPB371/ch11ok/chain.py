#類別的繼承

class Vehicle: #基礎類別
    def move(self):
        print('我是可以移動的交動工具')
        
class Bike(Vehicle): #衍生類別
    def move(self):
        Vehicle.move(self)
        print('但我必須以腳踏的方式來移動')

class Child_Bike(Bike): #孫類別
    def move(self):
        Bike.move(self)
        print('為了小朋友的安全我特別加上輔助輪')

#產生孫類別實體
small_giant = Child_Bike()
small_giant.move()
