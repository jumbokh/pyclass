#類別的繼承

class Vehicle: #基礎類別
    def move(self):
        print('我是可以移動的交動工具')
        
class Bike(Vehicle): #衍生類別
    def move(self):
        Vehicle.move(self)
        print('但我必須以腳踏的方式來移動')

#產生子類別實體
giant = Bike()
giant.move()
