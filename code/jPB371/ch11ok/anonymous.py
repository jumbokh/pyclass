class Rectangle:
	def __init__(self, length=10, width=5):
		self.length=length
		self.width=width

	def getArea(self):
		return self.length* self.width

print("透過init()方法預設值的面積: ",Rectangle().getArea())

print("透過init()方法傳入參數的面積: ",Rectangle(125,6).getArea())
