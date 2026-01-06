from tkinter import Tk
from tkinter import ttk as t

def myfunc():
    print(f"called '{myfunc.__name__}'.")

root = Tk()
frm = t.Frame(root, padding=10)
frm.grid()
t.Label(frm, text="Hello World!").grid(column=0, row=0)
quit_btn = t.Button(frm, command=myfunc,text="gr")
quit_btn.grid(column=1, row=0)

root.mainloop()
