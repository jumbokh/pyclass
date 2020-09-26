# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("300x100")
win.title("place")

btn1=tk.Button(win, width=20, text="這是按鈕1")
btn1.place(x=0, y=0)
btn2=tk.Button(win, width=20, text="這是按鈕2")
btn2.place(relx=0.5, rely=0.5, anchor="center")
btn3=tk.Button(win, width=20, text="這是按鈕3")
btn3.place(relx=0.5, rely=0.7)

win.mainloop()