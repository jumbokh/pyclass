# 以Menu元件建置功能表
from tkinter import *

# 定義回應函式
def NewFile():
    print('New File!')
    
def OpenFile():
    file = filedialog.askopenfilename()
    print(file)

def SaveFile():
    save = filedialog.asksaveasfilename()
    
def About():
    print('這是一個很簡單的功能表')

wnd = Tk()#主視窗物件
wnd.title('功能表')

# Step1.產生功能表物件menuBar，Menu加到主視窗物件
menuBar = Menu(wnd)

# Step2.將功能表物件menubar佈置到主視窗的頂部，顯示於畫面
wnd.config(menu = menuBar)

# Step3.加入主功能表項目
menu_file = Menu(menuBar, tearoff = 0)
menu_font = Menu(menuBar, tearoff = 0)
menu_help = Menu(menuBar, tearoff = 0)

# Step4. add_cascade()方法產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字型', menu = menu_font)
menuBar.add_cascade(label = '線上說明', menu = menu_help)

# Step5. 加入下拉選單的項目 Step5-1. File主能表表
menu_file.add_command(label = '新檔案',
        command = NewFile)
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = OpenFile)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        command = SaveFile)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        command = lambda : wnd.destroy())

# Step5-2. Font主功能表
labels = (12, 14, 16, 18)
for item in labels:
    menu_font.add_radiobutton(label = item)

# Step5-3. Help主功能表
menu_help.add_command(label = '關於', command = About)

mainloop()
