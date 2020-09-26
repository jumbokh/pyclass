# -*- coding: utf-8 -*-
"""
程式名稱：簡易單字翻譯機
題目要求：
讓使用者輸入單字之後，點選「中翻英」顯示英文，點選「英翻中」顯示中文

"""
def ctoe():
    i = entry.get()     #取得entry元件輸入的內容
    ans=""
    for k,v in dictionary.items():
        if v == i:
            ans = k
            break
   
    if ans:
        label.config(text = ans)  #在label元件顯示文字
    else:
        label.config(text = "找不到["+i+"]")  #在label元件顯示文字


def etoc():
    i = entry.get()     #取得entry元件輸入的內容
    ans = dictionary.get(i,"找不到["+i+"]")
    label.config(text = ans)  #在label元件顯示文字

def clear():  
    entry.delete(0, "end")
    label.config(text = "")    



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