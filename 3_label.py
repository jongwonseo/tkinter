from tkinter import *

root = Tk()
root.title("GUI")

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file = r'C:\Users\JDoubleU\Desktop\프로그래밍\tkinter_practice\check.png')

label2 = Label(root, image=photo)
label2.pack()

def config():
  label1.config(text="또 만나요")

  global photo2
  photo2 = PhotoImage(file = r'C:\Users\JDoubleU\Desktop\프로그래밍\tkinter_practice\x.png')
  label2.config(image=photo2) #garbage collector
btn = Button(root, text="클릭", command = config)
btn.pack() 

root.mainloop()