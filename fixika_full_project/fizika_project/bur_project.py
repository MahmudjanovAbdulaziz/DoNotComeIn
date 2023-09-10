from tkinter import *


def btn_x():
    btn_next.pack_forget()
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    lab1.pack_forget()
    l.pack_forget()
    btn_next.pack_forget()
    lab2.pack_forget()
    t.pack_forget()
    btn_xx.pack()
    lab3.pack_forget()
    lab_a.pack_forget()
    lab_config.pack_forget()
    lab_b.pack_forget()
    btn_next.pack_forget()
    btn_next_los.pack_forget()
    lab_definition.pack_forget()
    btn_xx.pack_forget()
    lab_otv.pack_forget()
    lab_two_1.pack_forget()
    H.pack_forget()
    t_mech.pack_forget()
    lab_two_2.pack_forget()
    lab_otv_1.pack_forget()
    lab_definition_1.pack_forget()
    lab_print_1.pack_forget()
    lab_a_1.pack_forget()
    lab_a_2.pack_forget()
    lab_config_1.pack_forget()
    lab_otv_4.pack_forget()
    lab_otv.pack_forget()
    lab_definet_2.pack_forget()
    lab_config_plus.pack_forget()
    lab_a_6.pack_forget()
    lab_config_plus.pack_forget()
    lab_a_5.pack_forget()
    lab_a_4.pack_forget()
    lab_config.pack_forget()
    lab_a_3.pack_forget()
    label_input.pack_forget()
    lab_config_plus_2.pack_forget()
    lab_two_2.pack_forget()
    t_mech_2.pack_forget()
    lab_two_doun.pack_forget()
    t_doun.pack_forget()
    lab_two_state.pack_forget()
    t_state.pack_forget()
    btn_next_start.pack_forget()
    lab_otv.pack_forget()
    lab_pds_otv_l.pack_forget()
    lab_metr_2.pack_forget()
    lab_definition_2.pack_forget()
    lab_metr.pack_forget()
    lab_config_3.pack_forget()
    lab_metr.pack_forget()
    lab3.pack_forget()
    btn_next_1.pack_forget()
    t_state.pack_forget()
    lab_two_1.pack_forget()
    h.pack_forget()
    lab_two_2.pack_forget()
    t_mech_2.pack_forget()
    lab_two_doun.pack_forget()
    t_doun.pack_forget()
    lab_two_state.pack_forget()
    t_state.pack_forget()
    btn_next_2.pack_forget()
    lab_wccr_final.pack_forget()
    lab_wccr.pack_forget()
    lab_print_1.pack_forget()
    lab_constructive_walls.pack_forget()
    lab_drilled.pack_forget()
    lab_config.pack_forget()
    lab3.pack_forget()
    lab1.pack_forget()
    h_drilled.pack_forget()
    lab_constructive_walls.pack_forget()
    t_constructive_wallas.pack_forget()
    btn_constructive_walls.pack_forget()
    lab_Value_Error.pack_forget()
    lab_distance.pack_forget()
    h_entry.pack_forget()
    lab_pds.pack_forget()
    t_entry.pack_forget()
    btn_next_start.pack_forget()


def speed_1():
    btn2.pack_forget()
    btn3.pack_forget()
    btn1.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab1.pack()
    l.pack()
    btn_next.pack()
    lab2.pack()
    t.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def speed_2():
    btn2.pack_forget()
    btn3.pack_forget()
    btn1.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab_two_1.pack()
    H.pack()
    btn_next.pack()
    lab_two_2.pack()
    t_mech.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def final():
    try:
        lab1.pack_forget()
        l.pack_forget()
        btn_next.pack_forget()
        lab2.pack_forget()
        t.pack_forget()
        lab3.pack()
        lab_a['text'] = l.get()
        lab_a.pack()
        lab_config.pack()
        lab_b['text'] = t.get()
        lab_b.pack()
        btn_next_los.pack()
        lab_definition.pack()
        dept_l = float(l.get())
        dept_t = float(t.get())
        dept_otv = dept_t / dept_l
        label_input['text'] = dept_otv.__getnewargs__()
        lab_print_1.pack()
        label_input.pack()
    except ValueError:
        lab_Value_Error.pack()


def mechanick():
    btn1.pack_forget()
    btn2.pack_forget()
    btn3.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab_two_1.pack()
    H.pack(anchor=S, padx=40, pady=0)
    lab_two_2.pack()
    t_mech.pack()
    btn_next_1.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def next_2():
    try:
        btn_next_1.pack_forget()
        lab_a_1['text'] = H.get()
        lab_a_1.pack()
        lab_config_1.pack()
        lab_a_2['text'] = t_mech.get()
        lab_a_2.pack()
        lab_two_1.pack_forget()
        H.pack_forget()
        lab_two_2.pack_forget()
        t_mech.pack_forget()
        temp_1 = float(H.get())
        temp_2 = float(t_mech.get())
        temp_otv = temp_1 / temp_2
        lab_otv_1['text'] = temp_otv.__getnewargs__()
        lab_print_1.pack()
        lab_otv_1.pack()
        lab_definition_1.pack()
    except ValueError:
        lab_Value_Error.pack()


def start_1():
    btn1.pack_forget()
    btn2.pack_forget()
    btn3.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab_two_1.pack()
    h.pack()
    lab_two_2.pack()
    t_mech_2.pack()
    lab_two_doun.pack()
    t_doun.pack()
    lab_two_state.pack()
    t_state.pack()
    btn_next_2.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def btn_next_two():
    try:
        btn_next_2.pack_forget()
        btn_next_1.pack_forget()
        lab_two_1.pack_forget()
        h.pack_forget()
        lab_two_2.pack_forget()
        t_mech_2.pack_forget()
        lab_two_doun.pack_forget()
        t_doun.pack_forget()
        lab_two_state.pack_forget()
        t_state.pack_forget()
        temp_1_1 = float(h.get())
        temp_1_2 = float(t_mech_2.get())
        temp_1_3 = float(t_doun.get())
        temp_1_4 = float(t_state.get())
        temp_1_otv = temp_1_1 / (temp_1_2 + temp_1_3 + temp_1_4)
        lab_a_3['text'] = h.get()
        lab_a_3.pack()
        lab_config.pack()
        lab_a_4['text'] = t_mech_2.get()
        lab_a_4.pack()
        lab_config_plus.pack()
        lab_a_5['text'] = t_doun.get()
        lab_a_5.pack()
        lab_config_plus_2.pack()
        lab_a_6['text'] = t_state.get()
        lab_a_6.pack()
        lab_otv_4['text'] = temp_1_otv.__getnewargs__()
        lab_definet_2.pack()
        lab_otv.pack()
        lab_otv_4.pack()
    except ValueError:
        lab_Value_Error.pack()


def technical_drilling():
    btn1.pack_forget()
    btn2.pack_forget()
    btn3.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab_distance.pack()
    h_entry.pack()
    lab_pds.pack()
    t_entry.pack()
    btn_next_start.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def next_in():
    try:
        lab_two_2.pack_forget()
        t_mech_2.pack_forget()
        lab_two_doun.pack_forget()
        t_doun.pack_forget()
        lab_two_state.pack_forget()
        t_state.pack_forget()
        btn_next_start.pack_forget()
        lab_distance.pack_forget()
        h_entry.pack_forget()
        lab_pds.pack_forget()
        t_entry.pack_forget()
        btn_next_start.pack_forget()
        lab3.pack()
        lab_metr['text'] = h_entry.get()
        lab_metr.pack()
        lab_config_3.pack()
        lab_metr.pack()
        lab_metr_2['text'] = t_entry.get()
        lab_metr_2.pack()
        lab_definition_2.pack()
        lab_metr_otv = float(h_entry.get())
        lab_time_otv = float(t_entry.get())
        lab_pds_otv = lab_metr_otv / lab_time_otv
        lab_pds_otv_l['text'] = lab_pds_otv.__getnewargs__()
        lab_otv.pack()
        lab_pds_otv_l.pack()
    except ValueError:
        lab_Value_Error.pack()


def btn_5():
    btn1.pack_forget()
    btn2.pack_forget()
    btn3.pack_forget()
    btn4.pack_forget()
    btn5.pack_forget()
    lab1.pack()
    h_drilled.pack()
    lab_constructive_wall.pack()
    t_constructive_wallas.pack()
    btn_constructive_walls.pack()
    btn_xx.pack(anchor=SW, padx=6, pady=6)


def constructive_next():
    try:
        lab1.pack_forget()
        h_drilled.pack_forget()
        lab_constructive_wall.pack_forget()
        t_constructive_wallas.pack_forget()
        btn_constructive_walls.pack_forget()
        lab3.pack()
        lab_drilled['text'] = h_drilled.get()
        lab_drilled.pack()
        lab_config.pack()
        lab_constructive_walls['text'] = t_constructive_wallas.get()
        lab_constructive_walls.pack()
        lab_wccr.pack()
        lab_print_1.pack()
        lab_drilled_fin = float(h_drilled.get())
        lab_const = float(t_constructive_wallas.get())
        labwccr = lab_drilled_fin / lab_const
        lab_wccr_final['text'] = labwccr.__getnewargs__()
        lab_wccr_final.pack()
    except ValueError:
        lab_Value_Error.pack()


root = Tk()
root.resizable(width=False, height=False)
root.title('ВСБ')
root.geometry('600x600')
root['bg'] = 'black'

btn1 = Button(root,
              text='Скорость бурения',
              bg='white',
              fg='red',
              padx=250,
              pady=10,
              font='Arial 14',
              activeforeground='lime',
              activebackground='red',
              command=speed_1)

btn2 = Button(root,
              text='Механическая скорость бурения',
              bg='white',
              fg='red',
              padx=250,
              pady=10,
              font='Arial 14',
              activeforeground='lime',
              activebackground='red',
              command=mechanick)

btn3 = Button(root,
              text='Рейсовая скорость бурения ',
              bg='white',
              fg='red',
              padx=250,
              pady=10,
              font='Arial 14',
              activeforeground='lime',
              activebackground='red',
              command=start_1
              )

btn4 = Button(root,
              text='Техническая скорость бурения',
              bg='white',
              fg='red',
              padx=250,
              pady=10,
              font='Arial 14',
              activeforeground='lime',
              activebackground='red',
              command=technical_drilling
              )

btn5 = Button(root,
              text='Цикловая скорость строительства скважины',
              bg='white',
              fg='red',
              padx=250,
              pady=10,
              font='Arial 14',
              activeforeground='lime',
              activebackground='red',
              command=btn_5
              )

btn_next = Button(root,
                  text='➔',
                  bg='lime',
                  fg='blue',
                  activebackground='lime',
                  activeforeground='blue',
                  padx=50,
                  pady=5,
                  command=final)

btn_next_los = Button(root,
                      text='➔',
                      bg='lime',
                      fg='blue',
                      activebackground='lime',
                      activeforeground='blue',
                      padx=50,
                      pady=5,
                      command=speed_1)

btn_xx = Button(root,
                text='x',
                bg='red',
                fg='black',
                padx=6,
                pady=6,
                command=btn_x
                )

btn_next_1 = Button(root,
                    text='➔',
                    bg='lime',
                    fg='blue',
                    activebackground='lime',
                    activeforeground='blue',
                    padx=50,
                    pady=5,
                    command=next_2
                    )

btn_next_2 = Button(root,
                    text='➔',
                    bg='lime',
                    fg='blue',
                    activebackground='lime',
                    activeforeground='blue',
                    padx=50,
                    pady=5,
                    command=btn_next_two
                    )

btn_next_start = Button(root,
                        text='➔',
                        bg='lime',
                        fg='blue',
                        activebackground='lime',
                        activeforeground='blue',
                        padx=50,
                        pady=5,
                        command=next_in)

btn_constructive_walls = Button(root,
                                text='➔',
                                bg='lime',
                                fg='blue',
                                activebackground='lime',
                                activeforeground='blue',
                                padx=50,
                                pady=5,
                                command=constructive_next

                                )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
lab_print_1 = Label(root,
                    text='Ответ:',
                    padx=20,
                    pady=10,
                    bg='black',
                    fg='white'
                    )

lab1 = Label(root,
             text='Количество пробуренных метров ',
             padx=20,
             pady=10,
             bg='black',
             fg='white')
lab2 = Label(root,
             text='Время бурения в мин ',
             padx=20,
             pady=10,
             bg='black',
             fg='white')
lab3 = Label(root,
             text='Решение:',
             padx=20,
             pady=10,
             bg='black',
             fg='white')

lab_a = Label(root,
              text='',
              padx=20,
              pady=10,
              bg='black',
              fg='white')

lab_config = Label(root,
                   text='/',
                   padx=30,
                   pady=10,
                   bg='black',
                   fg='white')

lab_config_plus = Label(root,
                        text='+',
                        padx=30,
                        pady=10,
                        bg='black',
                        fg='white')

lab_config_plus_2 = Label(root,
                          text='+',
                          padx=30,
                          pady=10,
                          bg='black',
                          fg='white')

lab_b = Label(root,
              text='',
              padx=30,
              pady=10,
              bg='black',
              fg='white')

lab_drilled = Label(root,
                    text='',
                    padx=20,
                    pady=10,
                    bg='black',
                    fg='white')

lab_constructive_walls = Label(root,
                               text='',
                               padx=20,
                               pady=10,
                               bg='black',
                               fg='white')

lab_wccr_final = Label(root,
                       text='',
                       padx=30,
                       pady=10,
                       bg='black',
                       fg='white')

lab_Value_Error = Label(root,
                        text='Нельзя разделить строку с числом!!!',
                        padx=20,
                        pady=10,
                        bg='black',
                        fg='white')

lab_definition = Label(root,
                       text='Определение: \n1). Коммерческая скорость \n(в метрах на станко/месяц) определяется \nотношением количества пробуренных метров \nк календарному времени бурения, \nвключающее непроизводительное время \n(организационные простои, ликвидации аварий)',
                       padx=30, pady=10, bg='black', fg='white')

lab_definition_1 = Label(root,
                         text='Определение \nМеханическая скорость бурения -\n количество метров бурения за 1 \nчас работы долота на забое',
                         padx=30, pady=10, bg='black', fg='white')

lab_definet_2 = Label(root,
                      text='Определение  \nРейсовая скорость бурения - \nколичество метров проходки ствола скважины, \nосуществляемой за один час рейса инструмента, \nт.е. времени работы долота на забое, \nспуске и подъеме инструмента',
                      padx=30, pady=10, bg='black', fg='white')

lab_definition_2 = Label(root,
                         text='Определение \nТехническая скорость бурения \nопределяется отношением проходки в метрах ко \nвремени технически необходимых работ по бурению, т.е. \nпроизводительному времени бурения, \nвыраженных в станко-месяцах',
                         padx=30, pady=10, bg='black', fg='white')

lab_wccr = Label(root,
                 text='Определение \nЦикловая скорость строительства скважины \nопределяется средней проходкой за время \nвышкомонтажных работ бурения, \nкрепления и испытания скважины, \nхарактеризует совместное действие бригад.',
                 padx=30, pady=10, bg='black', fg='white')

lab_otv = Label(root,
                text='Ответ: ',
                padx=30,
                pady=10,
                bg='black',
                fg='white',
                font='Arial 14')

lab_two_1 = Label(root,
                  text='Количество пробуренных метров:',
                  padx=20,
                  pady=10,
                  bg='black',
                  fg='white')

lab_two_2 = Label(root,
                  text='Время мех бурения в час:',
                  padx=20,
                  pady=10,
                  bg='black',
                  fg='white')

lab_a_1 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_config_1 = Label(root,
                     text='__',
                     padx=30,
                     pady=10,
                     bg='black',
                     fg='white')

lab_a_2 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_otv_1 = Label(root,
                  text='Ответ: ',
                  padx=30,
                  pady=10,
                  bg='black',
                  fg='white',
                  font='Arial 14')

lab_two_doun = Label(root,
                     text='Время Спусковой операции:',
                     padx=20,
                     pady=10,
                     bg='black',
                     fg='white')

lab_two_state = Label(root,
                      text='Время подготовительных работ:',
                      padx=20,
                      pady=10,
                      bg='black',
                      fg='white')

t_doun = Entry(root,
               width=15,
               font='Arial 20',
               bg='black',
               fg='lime')

t_state = Entry(root,
                width=15,
                font='Arial 20',
                bg='black',
                fg='lime')

lab_otv_2 = Label(root,
                  text='Ответ: ',
                  padx=30,
                  pady=10,
                  bg='black',
                  fg='white',
                  font='Arial 14')

lab_a_3 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_a_4 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_a_5 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_a_6 = Label(root,
                text='',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

label_input = Label(root,
                    text='',
                    padx=20,
                    pady=10,
                    bg='black',
                    fg='white')

lab_otv_4 = Label(root,
                  text='',
                  padx=20,
                  pady=10,
                  bg='black',
                  fg='white')

lab_distance = Label(root,
                     text='Количество пробуренных метров:',
                     padx=20,
                     pady=10,
                     bg='black',
                     fg='white')

lab_pds = Label(root,
                text='Продуктивное скорость бурения: ',
                padx=20,
                pady=10,
                bg='black',
                fg='white')

lab_metr = Label(root,
                 text='',
                 padx=20,
                 pady=10,
                 bg='black',
                 fg='white')

lab_config_3 = Label(root,
                     text='__',
                     padx=30,
                     pady=10,
                     bg='black',
                     fg='white')

lab_metr_2 = Label(root,
                   text='',
                   padx=20,
                   pady=10,
                   bg='black',
                   fg='white')

lab_pds_otv_l = Label(root,
                      text='',
                      padx=20,
                      pady=10,
                      bg='black',
                      fg='white')

lab_constructive_wall = Label(root,
                              text='Время строительства скважины',
                              padx=20,
                              pady=10,
                              bg='black',
                              fg='white')

t_entry = Entry(root,
                width=15,
                font='Arial 20',
                bg='black',
                fg='lime')

h_entry = Entry(root,
                width=15,
                font='Arial 20',
                bg='black',
                fg='lime')

h = Entry(root,
          width=15,
          font='Arial 20',
          bg='black',
          fg='lime')

t_mech_2 = Entry(root,
                 width=15,
                 font='Arial 20',
                 bg='black',
                 fg='lime')

l = Entry(root,
          width=15,
          font='Arial 20',
          bg='black',
          fg='lime')

t = Entry(root,
          width=15,
          font='Arial 20',
          bg='black',
          fg='lime')

H = Entry(root,
          width=15,
          font='Arial 20',
          bg='black',
          fg='lime')

t_mech = Entry(root,
               width=15,
               font='Arial 20',
               bg='black',
               fg='lime')

h_drilled = Entry(root,
                  width=15,
                  font='Arial 20',
                  bg='black',
                  fg='lime')

t_constructive_wallas = Entry(root,
                              width=15,
                              font='Arial 20',
                              bg='black',
                              fg='lime')

root.mainloop()
