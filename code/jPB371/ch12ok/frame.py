# -*- coding: utf-8 -*-


import tkinter as tk
win = tk.Tk()
win.title("Frame")

frm1 = tk.Frame(win, width=350, height=100, bg="green" )            
frm1.pack(side="left")

frm2 = tk.Frame(win, width=150, height=100, bg="yellow")       
frm2.pack(side="right")

win.mainloop()