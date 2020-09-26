class Rectangle:
	def __init__(self, length=10, width=5):
		self.length=length
		self.width=width

	def getArea(self):
		return self.length* self.width

R1=Rectangle()
print("透過init()方法預設值的面積: ",R1.getArea())

R2= Rectangle(125,6)
print("透過init()方法傳入參數的面積: ",R2.getArea())
