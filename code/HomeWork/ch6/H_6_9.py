cost = 100000
salvage = 10000
use = 200000
Actual_use = [10000,18000,12000,13000,15000,20000,25000,22000,28000,27000]
use_len = len(Actual_use)
def D_rate(A,B,C):
    return((A-B)/C)
def D_cost(A,B,C,D):
    row = []
    Acc_exp = 0
    balance = A
    result = []
    for x in range(0,D,1):
        exp = D_rate(A,B,C) * Actual_use[x]
        Acc_exp = Acc_exp + exp
        balance = balance - exp
        row.append(x+1)
        row.append(exp)
        row.append(Acc_exp)
        row.append(balance)
        result.append(row)
        row = []
    return(result)
r_table = D_cost(cost,salvage,use,use_len)
print('%3s%8s%8s%8s' %('年度','折舊費用','累計折舊','期末帳面價值'))
for i in range(0,use_len,1):
    print('%4d%10d%12d%14d' %(r_table[i][0],r_table[i][1],r_table[i][2],r_table[i][3]))
