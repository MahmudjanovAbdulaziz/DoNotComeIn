from tkinter import *
from tkinter import  messagebox
import random
import time


#Функция для закрытия программы
def close():
    if messagebox.askokcancel('Оповешение!', "Вы точно хотите выйти из программы?"):
        root.destroy()


#Создание окна root
root = Tk()
root.title('Информатика')
root.geometry('1360x760')
root.protocol("WM_DELETE_WINDOW", close)
root['bg'] = 'white'
root.iconbitmap('ico.ico')

#canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
#canvas.pack()

#Функция для выбора сложности
def choice_complexity():
    btn_start.place_forget()
    #Кнопка Легко
    #root.fon2 = PhotoImage(file='Background.png')
    #fon = Label(root, image=root.fon2)
    #fon.grid(row=0, column=0)
    btn_easy.place(x=500, y=0)
    btn_medium.place(x=500, y=100)
    btn_hard.place(x=500, y=200)

def esy_questions_1():
    root['bg'] = 'black'
    fon.grid_forget()
    #fon1.grid(row=0, column=0, )
    lab_question1_easy_1.place(x = 650, y = 200 , anchor=CENTER)
    yes_no.place(x=500, y=100)
    btn_otv1_esy_1.place(x = 500, y = 500, anchor=CENTER)
    btn_otv1_esy_2.place(x = 500, y = 400, anchor=CENTER)
    btn_otv1_esy_3.place(x = 500, y = 300, anchor=CENTER)
    btn_otv1_esy_4.place(x = 500, y = 200, anchor=CENTER)


#Фон в начале
root.fon = PhotoImage(file='fon.png')
fon = Label(root, image=root.fon)
fon.grid(row=0, column=0)

root.fon1 = PhotoImage(file='fon_1.png')
fon1 = Label(root, image=root.fon1)



#Кнопка старта
btn_start = Button( fon,
                   text='Start',
                   bg='light blue',
                   fg='gray',
                   activebackground='light blue',
                   activeforeground='lime',
                   font='Arial 14 bold',
                   width=30,
                   height=2,
                   highlightthickness=0,
                   bd=0,
                   command=choice_complexity)

btn_easy = Button(fon, text='Легко', font=('Comic Sans MS', 20, 'bold'), bg='light blue', fg='lime',
                  activebackground='green', activeforeground='lime', width=25, height=2, command=esy_questions_1 )

btn_medium = Button(fon, text='Среднее', font=('Comic Sans MS', 20, 'bold'), bg='light blue', fg='lime',
                    activebackground='orange', activeforeground='yellow', width=25, height=2)

btn_hard = Button(fon, text='Сложно', font=('Comic Sans MS', 20, 'bold'), bg='light blue', fg='lime',
                  activebackground='red', activeforeground='yellow', width=25, height=2)


lab_question1_easy_1 = Label(root, text='Единицей измерения информации является:',  bg='black', fg='lime', font='Arial 14', width=40, height=2)

btn_otv1_esy_1 = Button(root, text="Вольт", bg='light blue', fg='yellow', activeforeground='orange', activebackground='red', width=20, height=1)
btn_otv1_esy_2 = Button(root, text="Ампер", bg='light blue', fg='yellow', activeforeground='orange', activebackground='red', width=20, height=1)
btn_otv1_esy_3 = Button(root, text="Бит", bg='light blue', fg='yellow', activeforeground='green', activebackground='lime', width=20, height=1)
btn_otv1_esy_4 = Button(root, text="герц", bg='light blue', fg='yellow', activeforeground='orange', activebackground='red', width=20, height=1)

fon1.yes = PhotoImage(file='yes_no.png')
yes_no = Label(fon1, image=fon1.yes, highlightthickness=0, bd=0)
btn_yes_no = Button(fon1)

#Кнопка для запуска СТАРТ
btn_start.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()