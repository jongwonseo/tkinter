import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

def create_new_file():
  print("새 파일을 만듭니다.")

menu = Menu(root)

# file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="new file", command=create_new_file)
menu_file.add_command(label="new window")
menu_file.add_separator()
menu_file.add_command(label = "open file...")
menu_file.add_separator()
menu_file.add_command(label="save all", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="exit")

menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# view 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()