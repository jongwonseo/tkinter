import os
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x320")

# 열기, 저장, 파일 이름
filename = "mynote.txt"


def open_file():
  if os.path.isfile(filename): # 파일 있으면 T
    with open(filename, 'r', encoding='utf8') as file:
      txt.delete('1.0', END) # 본문 삭제
      txt.insert(END, file.read()) #본문 입력

def save_file():
  with open(filename, 'w', encoding='utf8') as file:
    file.write(txt.get('1.0', END))


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=open)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식, 보기, 도움말
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.resizable(True, True)
root.mainloop()
