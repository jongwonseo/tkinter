import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # 가로x세로

Label(root, text="메뉴를 선택해 주세요").pack(side='top')

Button(root, text="주문하기").pack(side="bottom")
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side='left',expand=True, fill='both')

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="차칸버거").pack()

frame_drink = LabelFrame(root, text="음료")
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
frame_drink.pack(side='right', expand=True, fill='both')


root.mainloop()