cost = 100000
salvage = 10000
n = 10
def D_cost(A,B,C):
    row = []
    Acc_exp = 0
    balance = A
    result = []
    reg = 0  
    for x in range(1,C+1,1):
        reg = reg + x
    for x in range(0,C,1):
        exp = round((((C-x)/reg) * (A-B)),0)
        Acc_exp = Acc_exp + exp
        balance = balance - exp
        row.append(x+1)
        row.append(exp)
        row.append(Acc_exp)
        row.append(balance)
        result.append(row)
        row = []
    return(result)
r_table = D_cost(cost,salvage,n)
print('%3s%8s%8s%8s' %('年度','折舊費用','累計折舊','期末帳面價值'))
for i in range(0,n,1):
    print('%4d%10d%12d%14d' %(r_table[i][0],r_table[i][1],r_table[i][2],r_table[i][3]))
