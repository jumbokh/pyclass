seller_1 = [33, 32, 56, 45, 33]
seller_2 = [77, 33, 68, 45, 23]
seller_3 = [43, 55, 43, 67, 65]
product_A = 12
product_B = 16
product_C = 10
product_D = 14
product_E = 15
def Total_sales(A,B,C,D,E):
    seller_total_1 = (seller_1[0] * A) + (seller_1[1] * B) +(seller_1[2] * C) + (seller_1[3] * D) + (seller_1[4] * E)
    seller_total_2 = (seller_2[0] * A) + (seller_2[1] * B) + (seller_2[2] * C) +(seller_2[3] * D) + (seller_2[4] * E)
    seller_total_3 = (seller_3[0] * A) + (seller_3[1] * B) + (seller_3[2] * C) +(seller_3[3] * D) + (seller_3[4] * E)
    return(seller_total_1,seller_total_2,seller_total_3)
print('第1位銷售員的銷售總額為 : %d 元 \n第2位銷售員的銷售總額為 : %d 元 \n第3位銷售員的銷售總額為 : %d 元' %(Total_sales(product_A,product_B,product_C,product_D,product_E)))

def Total_product_sales(A,B,C,D,E):
    product_A_sales = (seller_1[0] + seller_2[0] + seller_3[0]) * A
    product_B_sales = (seller_1[1] + seller_2[1] + seller_3[1]) * B
    product_C_sales = (seller_1[2] + seller_2[2] + seller_3[2]) * C
    product_D_sales = (seller_1[3] + seller_2[3] + seller_3[3]) * D
    product_E_sales = (seller_1[4] + seller_2[4] + seller_3[4]) * E   
    return(product_A_sales,product_B_sales,product_C_sales,product_D_sales,
product_E_sales)
print('第1項產品的銷售總額為 : %d 元 \n第2項產品的銷售總額為 : %d 元 \n第3項產品的銷售總額為 : %d 元 \n第4項產品的銷售總額為 : %d 元 \n第5項產品的銷售總額為 : %d 元' %(Total_product_sales(product_A,product_B,product_C,product_D,product_E)))

def High_sales_seller(A,B,C,D,E):
    sales = Total_sales(A,B,C,D,E)
    k = len(sales)
    High_sales_reg = sales[0]
    for m in range(0,k,1):    
        if sales[m] >= High_sales_reg:
            High_sales_reg = sales[m]
            seller = m+1
    return(seller)
print('有最好業績的銷售員是第 %d 位銷售員' %(High_sales_seller(product_A,product_B,product_C,product_D,product_E)))

def High_sales_product(A,B,C,D,E):
    sales_product = Total_product_sales(A,B,C,D,E)
    k = len(sales_product)
    High_sales_product_reg = sales_product[0]
    for m in range(0,k,1):
        if sales_product[m] >= High_sales_product_reg:
            High_sales_product_reg = sales_product[m]
            product = m+1
    return(product)
print('銷售總金額為最多的產品是第 %d 個產品' %(High_sales_product(product_A,product_B,product_C,product_D,product_E)))
