from tkinter import*


def get():
    label['text'] = lp.get()

root = Tk()
root.resizable(width=False, height=False)
root.title('физика')
root.geometry('600x600')
root['bg'] = 'black'

lp = Entry(root, width=20)
lp.pack(anchor=NW, padx=6, pady=6)

label = Label(root, text='text')
label.pack(anchor=NW, padx=6, pady=6)


root.mainloop()