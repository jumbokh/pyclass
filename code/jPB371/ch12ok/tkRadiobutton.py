from tkinter import *
wnd = Tk()
wnd.title('Radiobutton')
def myOptions():
    print('你的選項是 :', var.get())
ft = ('新細明體', 14)
Label(wnd, 
      text = "選擇喜愛的顏色", font = ft,
      justify = LEFT, padx = 20).pack()
color = [('紅色', 1), ('綠色', 2),
          ('藍色', 3)]
var = IntVar()
var.set(1)
for item, val in color:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 15,
        command = myOptions).pack(anchor = W)
