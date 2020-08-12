# H_5_1.py 功能:能夠計算出每一年的薪資所得、支出額、存款餘額
# 設定參數
salary = 30000 #薪資
expenses = 19000 #支出額
age = 25 #年齡
age_future = 28 #未來年齡
salary_rate = 0.03 #薪資成長率
exp_rate = 0.02 #支出額成長率
Deposit = 0 #存款餘額起始值為0
# 使用迴圈計算每一年的薪資所得、支出額、存款餘額
for n in range(age,age_future,1): 
    FV_salary = salary * (1+salary_rate)
    FV_expenses = expenses * (1+exp_rate)
    Deposit = Deposit + (FV_salary - FV_expenses)*12 
    salary = FV_salary # 將調整過的薪資覆蓋先前的薪資
    expenses = FV_expenses # 將調整過的支出額覆蓋先前的支出額
# 將結果印出來
print('薪資所得 : %d' %(round(FV_salary,0)))
print('支出額 : %d' %(round(FV_expenses,0)))
print('存款餘額 : %d' %(round(Deposit,0)))