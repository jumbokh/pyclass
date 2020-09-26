import os.path #匯入os.path
import sys

#利用isfile()方法先行判斷檔案是否存在
#如果檔案存在則取消複製工作
if os.path.isfile("introduct1.txt"):
    print("所指定開啟的檔案存在,不要進行複製")
    sys.exit()
else:
    #以open()方法開啟指定檔案,檔案開啟模式為"r"
    fb1=open("introduct.txt","r")
    #以open()方法開啟指定檔案,檔案開啟模式為"w"
    fb2=open("introduct1.txt","w")
    text=fb1.read() #以read()方法讀取檔案內容
    text=fb2.write(text) #以write()方法寫入檔案
    print("檔案複製工作完成,請開啟introduct1.txt查看")
    fb1.close() #以close()方法關閉檔案
    fb2.close() #以close()方法關閉檔案
