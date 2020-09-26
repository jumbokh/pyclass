# -*- coding: utf-8 -*-
"""
程式名稱：簡易計算機(GUI介面)
題目要求：
1.使用GUI介面,需有0~9.鍵、加減乘除(+-*/)鍵、Cls鍵(清除)
2.input區塊可用按鍵輸入也可用鍵盤輸入
3.容許錯誤輸入，輸出錯誤訊息「Infinity」. (例如輸入: 10/0，輸出:Infinity)
"""

def btn(root, text, row, col, w, colspan, command):   
    button = tk.Button(root, text=text, width=w, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, columnspan=colspan)

def get_input(argu):
    entry.insert("end",argu)   #將按鈕文字輸入entry元件
   

def calc():    
    try:
        input = entry.get()     #取得entry元件輸入的內容
        output = eval(input)    #取得運算結果
        entry.delete(0, "end")  #清除entry元件輸入的內容
        label.config(text = output)  #在label元件顯示文字
    except:
        label.config(text = "Infinity")   #在label元件顯示錯誤訊息
        

def clear():  
    entry.delete(0, "end")
    label.config(text = "")
    


import tkinter as tk
win = tk.Tk()
win.title("簡易計算機")

frame = tk.Frame(win)
frame.pack()
frame1 = tk.Frame(win)
frame1.pack()

entry = tk.Entry(frame, bg="#ffccff", font = "Helvetica 15 bold" ,borderwidth = 3)
entry.pack(fill="x")
label = tk.Label(frame, bg="#ffff00", font = "Helvetica 15 bold", anchor="e" , text = "計算結果")
label.pack(fill="x")


key=["123+", "456-", "789*", "0./"]
for x_index, x in enumerate(key):   
    for y_index, y in enumerate(x):
        btn(frame1, y, x_index, y_index, 6, 1, command=(lambda y=y : get_input(y)))


btn(frame1, 'Cls', 3, 3, 6, 1, command=clear)
btn(frame1, '=', 5, 0, 20, 4, command=calc)

win.mainloop()