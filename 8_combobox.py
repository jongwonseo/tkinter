import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.current(3) #디폴트값

values = [str(i)+"일" for i in range(1,32)]
readonly_combobox = ttk.Combobox(root, height = 10, values = values, state="readonly")
readonly_combobox.pack()
readonly_combobox.current(0) #0번째 인덱스값 선택

def btncmd():
  print(combobox.get())
  

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()