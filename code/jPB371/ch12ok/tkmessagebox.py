from tkinter import *
from tkinter import messagebox
wnd = Tk()
wnd.title('Messagebox訊息方塊')
wnd.geometry('180x120+20+50')
def answer():
    messagebox.showerror('回答',
            '抱歉！, 你的問題無法回答')
def callback():
    if messagebox.askyesno('訊息確認', 
            '真得要離開嗎？'):
        messagebox.showwarning('訊息 – Yes', 
            '抱歉!無法離開')
    else:
        messagebox.showinfo(   
            '訊息 – No', '取消「離開」指令')
Button(wnd, text='離開', command =
       callback).pack(side = 'left', padx = 10)
Button(wnd, text='回答', command =
       answer).pack(side = 'left')
mainloop()
