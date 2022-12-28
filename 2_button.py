from tkinter import *

root = Tk()
root.title("hihihiihihihihihihihihi")

# width, height: 버튼의 너비, 높이
# padx, pady: 버튼의 태두리와 내용의 가로여백, 세로여백


btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn5 = Button(root, fg='red', bg='yellow', text='버튼5')
btn5.pack()

# photo = PhotoImage(file = 'C:/Users/JDoubleU/Desktop/sample.jpg')
# btn6 = Button(root, image = photo)
# btn6.pack()

def btncmd():
  print("클릭 완료")

btn7 = Button(root, text='동작하는 버튼', command = btncmd)
btn7.pack()

root.mainloop()