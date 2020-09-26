#類別的繼承

class Animal: #基礎類別一
    def feature1(self):
        print('動物是多細胞真核生命體中的一大類群')
        
class Human: #基礎類別二
    def feature2(self):
        print('人類是一種具有情感高等智商動物')
        
class Boy(Animal, Human): #衍生類別
    pass

#產生子類別實體
Andy = Boy()
Andy.feature1()
Andy.feature2()
