import pandas as pd
import pandas_datareader.data as web
import fix_yahoo_finance as yf
from datetime import datetime
import numpy as np
from openpyxl import load_workbook

class TechnicalAnalysis:
      
    def rsi(n,roi):
        rslist=[]
        for i in range(n,roi.count()):
            u=0
            d=0
            for j in range(i-n+1,i+1):
                if roi[j]>=0:
                    u=u+roi[j]
                else:
                    d=d+roi[j]
            ups=u/n
            downs=abs(d/n)
            ud=ups/downs
            rslist.append(abs(100-(100/(1+ud))))
        return rslist
    
    def ma(df,n):
        malist=[]
        for i in range(n,len(df.index)+1):
            malist.append((sum(df[i-n:i]))/n)
        return malist
    
    def bias(df,n):
        bilist=[]
        for i in range(n,len(df.index)+1):
            bilist.append((df[i-1]-TechnicalAnalysis.ma(df,i)[0])/TechnicalAnalysis.ma(df,i)[0])
        return bilist


names = ['AAPL', 'GOOG', 'MSFT', 'DELL', 'GS', 'MS', 'BAC', 'C','3008.TW','2002.TW']

def get(stock, start, end):
    yf.pdr_override()
    #抓取時錯誤則回傳該股票錯誤資訊
    try:
        df=pd.DataFrame(web.get_data_yahoo(stock, start, end))
    except:
        print(stock+" error")
        return stock+" error"
    df2=pd.DataFrame(columns=['RSI6','MA6','BIAS6','RSI12','MA12','BIAS12','RSI20','MA20','BIAS20'],index=[df.index])
    
    def ss(n):  # 取得所有公式的資料
        rslist=TechnicalAnalysis.rsi(n,df[df.columns[0]].pct_change())
        malist=TechnicalAnalysis.ma(df['Close'],n)
        bilist=TechnicalAnalysis.bias(df['Close'],n)
        for i in range(n,len(df.index)-1):
            df2['RSI'+str(n)][i+1]=rslist.pop(0)
        for i in range(n,len(df.index)):
            df2['MA'+str(n)][i]=malist.pop(0)
            df2['BIAS'+str(n)][i]=bilist.pop(0)
    
    count=[6,12,20]    
    {n: ss(n) for n in count}  # 設定為6日、12日、20日
    
    return df2
            
#重複執行get迴圈，並每次匯入新的names[]資料進去
df2list = {n: get(n, datetime(2013, 1, 1),datetime(2013, 6, 1)) for n in names}
dictkey = list(df2list.keys())
dict_value =  list(df2list.values())

writer = pd.pandas.ExcelWriter('./H_8_4.xlsx') 
for i in range(0,len(df2list.keys())):
    #過濾錯誤的股票
    try:
        dict_value[i].to_excel(writer,sheet_name='%s' %(dictkey[i]))  # 分批資料匯入不同的工作表
    except:
        pass
writer.save()
#df2list