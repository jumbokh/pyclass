# simpledialog - askinteger()方法
from tkinter import *
from tkinter import simpledialog

def processWord(): #處理輸入字串    
    name = simpledialog.askstring(title = '輸入字串',
            prompt = '請輸入姓名: ')   
    print('名稱：', name)
   
def processInt(): #處理輸入整數值    
    score = []
    count = 0
    while True:
        number = simpledialog.askinteger(
            title = '輸入整數值', prompt = '分數: ',
            maxvalue = 100, minvalue = 60)
        score.append(number)
        count += 1
        if count == 5:
            break
    total = sum(score)    
    print('分數：', score)
    print('合計：', sum(score))
    

#建立視窗物件
wnd = Tk()
wnd.title('簡單型對話方塊')
wnd.geometry('140x60+10+10')
#視窗物件加入按鈕
Button(text = '輸入字串', command = processWord).pack(
    side = 'left')
Button(text = '輸入整數', command = processInt).pack(
    side = 'right', padx = 5)

mainloop()
