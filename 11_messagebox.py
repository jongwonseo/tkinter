import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # 가로x세로

#기차 예매
def info():
  msgbox.showinfo("알림", "정상적으로 예매 완료")

def warn():
  msgbox.showwarning("경고", "좌석 매진")

def error():
  msgbox.showwarning("에러", "결제 오류 발생")

def okcancel():
  msgbox.askokcancel("확인/취소", "해당 좌석은 유아 동반석입니다.")

def retrycancel():
  msgbox.askretrycancel("재시도/취소", "해당 좌석은 유아 동반석입니다.")

def yesno():
  msgbox.askyesno("예/아니요", "해당 좌석은 유아 동반석입니다.")

def yesnocancel():
  response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n자징 후 종료?")

  print("응답: ",response) # T,F,None = 1,0,다른 숫자

  if response == 1:
    print("ok")
  elif response == 0:
    print("no")
  else:
    print("cancel")

Button(root, command=info, text='infofo').pack()
Button(root, command=warn, text='warnrn').pack()
Button(root, command=error, text='error').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니요').pack()
Button(root, command=yesnocancel, text='예 아니요 취소').pack()

root.mainloop()