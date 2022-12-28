from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자 입력") #글자정보 입력할때

e = Entry(root, width=30)
e.pack()
e.insert(END, "한줄 입력")
#e.insert(END, "글자 입력") #글자정보 입력할때

def btncmd():
  # 내용 출력
  print(txt.get("1.0", END))  # "a.b"  a:첫번째 row,  b:b번째 column 위치
  print(e.get()) 

  # 내용 삭제
  txt.delete("1.0", END)
  e.delete(0, END)
btn = Button(root, text='클릭', command =btncmd)
btn.pack()


root.mainloop()