lis1=list(range(1,15,2))
lis1=lis1[slice(0,5)]
lis1=sorted(lis1,reverse=True)
lis1=lis1[slice(0,3)]
lis1=enumerate(lis1)
for i in lis1:
    print(i)