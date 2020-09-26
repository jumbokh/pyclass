# -*- coding: utf-8 -*-

def btn_click():
     btnvar.set("按下了按鈕1")

def btn1_click():
     btn1.config(fg = "red")  

import tkinter as tk
win = tk.Tk()
win.title("Button")
    
btnvar = tk.StringVar() 
btn = tk.Button(win, text="test", textvariable=btnvar, command=btn_click)
btnvar.set("這是按鈕1")
btn.pack(padx=20, pady=10)

btn1 = tk.Button(win, text="這是按鈕2", command=btn1_click)
btn1.pack(padx=20, pady=10)

win.mainloop()