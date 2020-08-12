import random
lis1=list(range(1,15,2))
lis1=lis1[slice(0,5,1)]
print(lis1)
num=random.randint(1,5)
print(num)
print(lis1[num-1])