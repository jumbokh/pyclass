from tkinter import *
wnd = Tk()
wnd.title('核取方塊')

def varStates(): #回應核取方塊變數狀態
   print('選取的科目有:', var1.get(), var2.get()
         ,var3.get())

ft1 =('微軟正黑體', 14)
ft2 = ('微軟正黑體', 14)
lb1=Label(wnd, text = '科目：', font = ft1)
lb1.grid(row = 0, column = 0)
item1 = '數學'
var1 = StringVar()
chk = Checkbutton(wnd, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk.grid(row = 0, column = 1)
item2 = '電腦'
var2 = StringVar()
chk2 = Checkbutton(wnd, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.grid(row = 0, column = 2)
item3 = '英文'
var3 = StringVar()
chk3 = Checkbutton(wnd, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.grid(row = 0, column = 3)

btnQuit = Button(wnd, text = '離開', font = ft2,
    command = wnd.destroy)
btnQuit.grid(row = 2, column = 1, pady = 4)
btnShow = Button(wnd, text = '顯示', font = ft2,
    command = varStates)
btnShow.grid(row = 2, column = 2, pady = 4)
mainloop()
