from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x320")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기')
menu_file.add_command(label='저장')
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)


root.resizable(True, True)

root.mainloop()
