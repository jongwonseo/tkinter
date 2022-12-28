from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x320")

chkvar = IntVar()
#체크박스 정보를 인트형으로 chkvar에 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) 

# chkbox.select() #자동 선택
# chkbox.deselect() #선택 해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", value = 222, variable=chkvar2)
chkbox2.pack()

def btncmd():
  print(chkvar.get()) #체크:1 해제:0
  print(chkvar2.get()) #체크:1 해제:0

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
