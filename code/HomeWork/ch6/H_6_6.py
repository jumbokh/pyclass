i = 0.12
def EAR_function(x):
    m = 1
    EAR_y = round((((1 + (x/m))**m) - 1)*100,2)
    m = 2
    EAR_h_y = round((((1 + (x/m))**m) - 1)*100,2)
    m = 4
    EAR_q = round((((1 + (x/m))**m) - 1)*100,2)
    m = 12
    EAR_m = round((((1 + (x/m))**m) - 1)*100,2)
    m = 365
    EAR_d = round((((1 + (x/m))**m) - 1)*100,2)   
    return(EAR_y,EAR_h_y,EAR_q,EAR_m,EAR_d)
print('年 : %.2f \n半年 : %.2f \n季 : %.2f \n月 : %.2f \n日 : %.2f' %(EAR_function(i)))
