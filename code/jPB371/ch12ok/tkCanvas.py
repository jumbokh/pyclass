from tkinter import *

root = Tk()
root.title('繪製線條及矩形')
gs = Canvas(root, width = 300, height = 300)
gs.pack()
gs.create_rectangle(
    50, 20, 200, 200, fill = '#AABBFF')
gs.create_rectangle(
    70, 40, 200, 200, fill = '#AACC69')
gs.create_rectangle(
    90, 60, 200, 200, fill = '#B9C8FF')
gs.create_rectangle(
    110, 80, 200, 200, fill = '#B886D0')

#左上角
gs.create_line(0, 0, 50, 20,
    fill = '#0E6042', width = 5)

mainloop()
