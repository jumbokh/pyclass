#以open()方法開啟指定檔案的文字檔
fb=open("introduct.txt","r")
#以read()方法讀取檔案內容
text=fb.read()
#輸入字串變數text的內容
print(text)
#以close()方法關閉檔案
fb.close()
