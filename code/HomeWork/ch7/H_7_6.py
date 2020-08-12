import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
from datetime import datetime
import matplotlib.pyplot as plt  # 使用matplotlib繪圖功能
import xlwings as xw            #可以使matplotlib的圖顯示在Excel上

yf.pdr_override()
df = pdr.get_data_yahoo("3008.TW",datetime(2013, 1, 1), datetime(2016, 4, 30))
#print(df.head())############
#df=web.DataReader("3008.TW", 'yahoo', datetime(2013, 1, 1), datetime(2016, 4, 30)) #資料期間過大 會計算一段時間
df['MA6']="NaN"
df['MA12']="NaN"
df['MA24']="NaN"
df['MA72']="NaN"
df['MA144']="NaN"
df['MA288']="NaN"

for i in range(6,len(df.index)+1):
    df.MA6[i-1]=((df['Close'][i-6:i].sum())/6)  # 從收盤價取前6天的資料加總後除以6得MA6
for i in range(12,len(df.index)+1):
    df.MA12[i-1]=((df['Close'][i-12:i].sum())/12)
for i in range(24,len(df.index)+1):
    df.MA24[i-1]=((df['Close'][i-24:i].sum())/24)
for i in range(72,len(df.index)+1):
    df.MA72[i-1]=((df['Close'][i-72:i].sum())/72)
for i in range(144,len(df.index)+1):
    df.MA144[i-1]=((df['Close'][i-144:i].sum())/144)
for i in range(288,len(df.index)+1):
    df.MA288[i-1]=((df['Close'][i-288:i])/288)
    
df.to_excel(pd.ExcelWriter('./H_7_6/H_7_6.xlsx'))

#2.
wb=xw.Book("./H_7_6/H_7_6.xlsx")
wb.sheets.add('MA')
fig=plt.figure()

plt.plot(df['MA6'])  # 將df['MA6']加入繪圖資料中
plt.plot(df['MA12'])
plt.plot(df['MA24'])
plt.plot(df['MA72'])
plt.plot(df['MA144'])
plt.plot(df['MA288'])
plt.legend(loc='best') # 顯示圖說
plt.grid()  # 顯示格線
plt.show()  # 繪圖
wb.sheets[0].pictures.add(fig, name='MA')

wb.save('./H_7_6/H_7_6.xlsx')