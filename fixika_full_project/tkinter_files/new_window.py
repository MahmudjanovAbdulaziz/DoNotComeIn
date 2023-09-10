from tkinter import  *
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel('Выход', "Вы точно хотите выйти из программы"):
        tk.destroy()

tk = Tk()
tk.title('Новое окно')
tk.resizable(0, 0)
tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.wm_attributes('-topmost', 1)

def new_windo1():
    new_window = Toplevel()
    new_window.title('Новое окно')
    new_window.resizable(0, 0)
    canvas = Canvas(new_window, width=300, height=300, highlightthickness=0, bd=0, bg='yellow')
    canvas.grid(row=0, column=0)


canvas = Canvas(tk, width=600, height=600, highlightthickness=0, bd=0, bg='red')
canvas.grid(row=0, column=0)

b0 = Button(tk, text='new window', command=new_windo1 )
b0.place(x=300, y=300)

tk.mainloop()
