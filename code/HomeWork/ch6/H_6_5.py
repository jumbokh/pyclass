Xi = [3,5,1,6,8,7]
Yi = [6,12,3,13,14,12]
k = len(Xi)

def co_var(X,Y):
    X_sum = 0    
    Y_sum = 0
    for m in range(0,k,1):
        X_sum = X_sum + X[m]
        Y_sum = Y_sum + Y[m]  
    Xii = X_sum / k
    Yii = Y_sum / k
    S_xy_sum = 0
    for n in range(0,k,1):  
        S_xy_sum += ((X[n] - Xii) * (Y[n] - Yii))
    S_xy = S_xy_sum / (k-1)      
    return(S_xy)
P = co_var(Xi,Yi)
print(P)
