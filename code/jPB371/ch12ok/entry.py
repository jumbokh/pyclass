# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.title("Entry")

entry = tk.Entry(win, bg="#ffccff", font = "Helvetica 15 bold" ,borderwidth = 3)
entry.insert(0,"這是Entry")
entry.insert("2","實用的")
entry.insert("end",",真好玩")
entry.pack(padx=20, pady=10)

win.mainloop()