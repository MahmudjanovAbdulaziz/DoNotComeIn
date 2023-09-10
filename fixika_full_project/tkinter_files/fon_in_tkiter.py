from tkinter import*

root = Tk()
root.title('Фон')
root.geometry('1300x1300')
root.resizable(width=False, height=False)

root.r  = PhotoImage(file='Gmail_Logo_512px.png')
bg_logo = Label(root, image=root.r)
bg_logo.grid(row=0, column=0)

btn = Button(root, text='HU_TAO', bg='black', fg='lime', font=('Comic Sans MS', 20, 'bold'))
btn.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()