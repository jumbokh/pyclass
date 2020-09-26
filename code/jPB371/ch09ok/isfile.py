import os.path #匯入os.path

#利用isfile()方法先行判斷檔案是否存在
#如果檔案存在則印出檔案內容
if os.path.isfile("resume.txt"):
    fb=open("resume.txt","r")
    for word in fb:
        print(word)
#如果檔案不存在則輸出檔案不存在的文字
else:
    print("所指定開啟的檔案不存在")
