#以open()方法開啟指定檔案的文字檔
fb=open("introduct.txt","r")
#將檔案指標移動到檔案的開頭處
fb.seek(0)
#以read(n)方法讀取檔案內容
text=fb.read(4)
#輸入字串變數text的內容
print(text)
#將檔案指標往前移動20個位元組
fb.seek(20)
#以read(n)方法讀取檔案內容
text=fb.read(13)
#輸入字串變數text的內容
print(text)
#以close()方法關閉檔案
fb.close()
