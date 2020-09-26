class Discount:
	def __init__(self, r=0.9):
		self.__rate=r

	def getRate(self):
		return self.__rate

	def howMuch(self):
		return money*self.__rate
money=10000
obj1=Discount(0.7)
print("此件商品的原有價格為",money,"元")
print("這件商品的折扣為", obj1.__rate)
print("打折扣後商品價格為", obj1.howMuch(),"元")
