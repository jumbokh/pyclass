import tkinter as tk
win = tk.Tk()
text=tk.Text(win)
text.insert(tk.INSERT, "Python的tk套件真好玩\n")
text.insert(tk.END, "結束文字方塊內容")
text.pack()
text.config(state=tk.DISABLED)
win.mainloop()
