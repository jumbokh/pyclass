# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("200x100")
win.title("常用widget")

label = tk.Label(win, bg="#ffff00", fg="#ff0000", font = "Helvetica 15 bold", padx=20, pady=5, text = "這是Label")
label.pack()

win.mainloop()