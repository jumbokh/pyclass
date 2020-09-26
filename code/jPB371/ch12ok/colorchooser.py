from tkinter import *
from tkinter import colorchooser

#調色盤方塊呼叫askcolor()方法讓使用者作顏色選取
def SelectColor():    
    tint = colorchooser.askcolor(title = '調色盤',
            initialcolor = '#FF88CC')    
    rgbs = tint[0]
    print('R: {:.3f}'.format(rgbs[0]))
    print('G: {:.3f}'.format(rgbs[1]))
    print('B: {:.3f}'.format(rgbs[2]))
    print('色彩16進位值:', tint[1])
#建立視窗物件
wnd = Tk()
wnd.title('提供色彩的colorchooser')
wnd.geometry('90x50+10+10')
#視窗物件加入按鈕
Button(text='調色盤', command = SelectColor).pack(
    side = 'bottom')
mainloop()
