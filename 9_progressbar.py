import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#   progressbar.stop()

# btn = Button(root, text="stop ", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=250, variable=p_var2)
progressbar2.pack()

def btn2cmd():
  for i in range(101):
    time.sleep(0.1) #0.01초 대기

    p_var2.set(i) # config()아님
    progressbar2.update()    # ui업데이트
    print(p_var2.get())

btn = Button(root, text="stop ", command=btn2cmd)
btn.pack()

root.mainloop()