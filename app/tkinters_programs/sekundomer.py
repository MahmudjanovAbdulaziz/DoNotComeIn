from tkinter import*
from datetime import*


temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)

def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def restart_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()

root = Tk()
root.title('Секундомер')
root.resizable(width=False, height=False)
root.geometry('300x200')

label1 = Label(root, width=10, font=('Comick Sans MS', 30), text='00:00')
label1.pack()

btnStart = Button(root, text="Старт", font=('Comick Sans MS', 20), width=15, command=start_tick, bg='yellow', fg='lime')
btnStop = Button(root, text="Стоп", font=('Comick Sans MS', 20), width=15, command=stop_tick, bg='yellow', fg='lime')
btnContinue = Button(root, text="Продолжить", font=('Comick Sans MS', 20), width=15, command=continue_tick, bg='yellow', fg='lime')
btnReset = Button(root, text="Сброс", font=('Comick Sans MS', 20), width=15, command=restart_tick, bg='yellow', fg='lime')
btnStart.pack()







root.mainloop()