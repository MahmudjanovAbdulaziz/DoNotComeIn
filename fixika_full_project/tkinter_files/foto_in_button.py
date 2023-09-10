from tkinter import *
from tkinter import messagebox

def close():
    if messagebox.showinfo('Оповешение!', "Вы точно хотите выйти из программы?"):
        tk.destroy()


def click_red():
    canvas.configure(bg='red')
    img1.configure(bg='red', activebackground='red')
    img2.configure(bg='red')

def click_white():
    canvas.configure(bg='white')
    img1.configure(bg='white', activebackground='red')
    img2.configure(bg='white', activebackground='white')

tk = Tk()
tk.title('Мое приложение')
tk.resizable(width=False, height=False)
tk.wm_attributes('-topmost', 1)
tk.protocol("WM_DELETE_WINDOW", close)

canvas = Canvas(tk, width=600, height=600, highlightthickness=0)
canvas.pack()

our_button = PhotoImage(file="Gmail_Logo_512px.png")
our_button = our_button.subsample(4, 4)
#id_img1 = canvas.create_image(200, 100, anchor='nw', image=our_button)
img1 = Button(tk, text='it is Button new programm', image=our_button, highlightthickness=0, bd=0, command=click_red, fg='black')
img1.place(x=300, y=150, anchor=CENTER)

img2 = Button(tk, image=our_button, highlightthickness=0, bd=0, command=click_white)
img2.place(x=300, y=450, anchor=CENTER)




tk.mainloop()