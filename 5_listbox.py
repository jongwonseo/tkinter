from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x320")

listbox = Listbox(root, selectmode = "extended", height = 3) # 디폴트 height = 0 
listbox.insert(0, "사과")
listbox.insert(END, "수박")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
  listbox.delete(END)
  # listbox.delete(0) 앞에거 삭제
  
  listbox.insert(END, "ㅋㅋㅋㅋ")
  
  # 개수
  print(listbox.size())

  #항목 확인
  print(listbox.get(0,listbox.size()-1))

  #선택된 항목 확인(인덱스로 반환)
  print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command = btncmd)
btn.pack()
root.mainloop()
