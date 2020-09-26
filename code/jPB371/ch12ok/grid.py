# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("300x100")
win.title("grid")

btn1=tk.Button(win, width=20, text="這是按鈕1")
btn1.grid(column=0,row=0)
btn2=tk.Button(win, width=20, text="這是按鈕2")
btn2.grid(column=0,row=1)
btn3=tk.Button(win, width=20, text="這是按鈕3")
btn3.grid(column=1,row=0)
btn4=tk.Button(win, width=20, text="這是按鈕4")
btn4.grid(column=2,row=1)
win.mainloop()