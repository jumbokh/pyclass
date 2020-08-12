program_A = [-3000,1900,1100,800,300]
program_B = [-3000,600,800,1200,2000]
program_C = [-1500,500,1200,150,160] 
n = len(program_A)
k = 0.05

def NPV_function(x,y):
    NPV_A = 0
    NPV_B = 0
    NPV_C = 0
    for i in range(0,x,1):
        NPV_A = NPV_A + program_A[i]/(1+y)**i
        NPV_B = NPV_B + program_B[i]/(1+y)**i
        NPV_C = NPV_C + program_C[i]/(1+y)**i
    return(NPV_A,NPV_B,NPV_C)
print('A方案的NPV為: $%.2f \nB方案的NPV為: $%.2f \nC方案的NPV為: $%.2f' %(NPV_function(n,k)))
