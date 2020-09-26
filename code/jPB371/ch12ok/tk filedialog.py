''' filedialog.askopenfile()方法開啟檔案
    filedialog.asksaveasfile()方法儲存檔案 '''

from tkinter import *
from tkinter import filedialog

#開啟檔案對話方塊
def OpenFile(): 
    name = filedialog.askopenfilename(title = '開啟檔案',
            filetypes = [('Text File', '*.txt'),
            ('Python Files', '*.py *.pyw'),
            ('All Files', '*')])
    print('開啟的檔案', name)
    #建立檔案 -- 使用open()函式
    with open('myfile.txt', 'rt') as foin:
        total = foin.read()
        print('字元數：', len(total))
        for line in total:    
            print(line, end = '')
            
#儲存檔案
def SaveFile():    
    save = filedialog.asksaveasfilename(title = '儲存檔案',
            filetypes = [('Text Files', '*.txt *.csv')],
            initialfile = 'myfile.txt')
    #以附加寫入檔案
    with open('myfile.txt', 'a+') as fout:
        show = '天道酬勤 地道酬善\n'
        print('字串長度：', len(show))
        fout.write(show)        
    print('儲存檔案', save)

#建立視窗物件
wnd = Tk()
wnd.title('filedialog')
wnd.geometry('100x50+10+10')

#視窗物件加入兩個按鈕
Button(text='開啟檔案', command = OpenFile).pack(
    anchor = 's', side = 'left', padx = 10)
Button(text='儲存檔案', command = SaveFile).pack(
    anchor = 's', side = 'left')
mainloop()
