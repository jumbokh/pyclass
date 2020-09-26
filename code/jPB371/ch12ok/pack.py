# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("300x100")
win.title("pack")

btn1=tk.Button(win, width=25, text="這是按鈕1")
btn1.pack()
btn2=tk.Button(win, width=25, text="這是按鈕2")
btn2.pack()
btn3=tk.Button(win, width=25, text="這是按鈕3")
btn3.pack()

win.mainloop()