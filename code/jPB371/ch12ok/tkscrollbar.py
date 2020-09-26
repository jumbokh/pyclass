from tkinter import *

Window = Tk()
scrollbar = Scrollbar(Window)
scrollbar.pack( side = RIGHT, fill = Y )

test_List = Listbox(Window, yscrollcommand = scrollbar.set )
for line in range(20):
   test_List.insert(END, "目前所在的行數: " + str(line+1))

test_List.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = test_List.yview )

mainloop()
