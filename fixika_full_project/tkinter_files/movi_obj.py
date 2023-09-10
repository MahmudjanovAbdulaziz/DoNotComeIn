from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel('Выход из программы', 'Вы точно хотите выйти из программы?'):
        tk.destroy()


tk = Tk()
tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.title('Двигать предметы')
tk.resizable(width=False, height=False)

canvas = Canvas(tk, width=700, height=700, highlightthickness=0)
canvas.pack()

canvas1 = Canvas(tk, width=100, height=100)
canvas1.place(x=300, y=300, anchor=CENTER)
canvas1.create_rectangle(0, 0, 100, 100, fill='red')

canvas2 = Canvas(tk, width=100, height=100)
canvas2.place(x=300, y=300, anchor=CENTER)
canvas2.create_oval(5, 5, 95, 95, fill='red')
canvas2.create_oval(10, 10, 90, 90, fill='yellow')

canvas3 = Canvas(tk, width=100, height=100)
canvas3.place(x=300, y=100, anchor=CENTER)
canvas3.create_rectangle(0, 0, 100, 100, fill='green')

canvas4 = Canvas(tk, width=100, height=100)
canvas4.place(x=400, y=100, anchor=CENTER)
canvas4.create_line(0, 0, 100, 100, )

canvas5 = Canvas(tk, width=100, height=100)
canvas5.place(x=500, y=200, anchor=CENTER)
canvas5.create_rectangle(0, 0, 100, 100, fill='orange')

canvas6 = Canvas(tk, width=100, height=100)
canvas6.place(x=500, y=300, anchor=CENTER)
canvas6.create_rectangle(0, 0, 100, 100, fill='lime')

canvas7 = Canvas(tk, width=100, height=100)
canvas7.place(x=500, y=400, anchor=CENTER)
canvas7.create_rectangle(0, 0, 100, 100, fill='yellow')


def drag(event):
    # print(event.x_root, event.x_root)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)
    event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)


canvas1.bind("<B1-Motion>", drag)
canvas2.bind("<B1-Motion>", drag)
canvas3.bind("<B1-Motion>", drag)
canvas5.bind("<B1-Motion>", drag)
canvas6.bind("<B1-Motion>", drag)
canvas7.bind("<B1-Motion>", drag)

tk.mainloop()
