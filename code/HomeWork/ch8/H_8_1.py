class test:
    def add(self,n):
        self.s=0
        for i in range(1,n+1):
            self.s+=i
        return self.s
        
    def mult(self,n):
        self.t=1
        for i in range(1,n+1):
            self.t*=i
        return self.t
        
test1=test()
s=int(input('輸入一個正整數n累加:'))
print(test1.add(s))
t=int(input('輸入一個正整數n累乘:'))
print(test1.mult(t))