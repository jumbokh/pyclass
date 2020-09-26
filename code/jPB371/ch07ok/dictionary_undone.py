# -*- coding: utf-8 -*-
"""
程式名稱：簡易單字翻譯機
題目要求：
讓使用者輸入單字之後，點選「中翻英」顯示英文，點選「英翻中」顯示中文

**此為練習檔,尚未完成,請自行加入ctoe()、etoc()及clear()函數
"""




dictionary = {'bird':'鳥', 'cat':'貓', 'dog':'狗', 'pig':'豬'}        


#GUI介面
import tkinter as tk
win = tk.Tk()
win.title("簡易單字翻譯機")

frame = tk.Frame(win)
frame.pack(padx=5, pady=5)
frame1 = tk.Frame(win)
frame1.pack(padx=5, pady=5)

entry = tk.Entry(frame, bg="#99ffcc", font = "JhengHei 15" ,borderwidth = 3)
entry.config(width=10)
entry.grid(column=0,row=0)

label = tk.Label(frame, bg="#ffffcc", font = "JhengHei 15", text = "")
label.config(width=10)
label.grid(column=1,row=0)

btnCtoe = tk.Button(frame1, text="中翻英", command=ctoe)
btnCtoe.grid(column=0,row=0)
btnEtoc = tk.Button(frame1, text="英翻中", command=etoc)
btnEtoc.grid(column=1,row=0)
btnClear = tk.Button(frame1, text="　清　除　", command=clear)
btnClear.grid(column=2,row=0)
win.mainloop()