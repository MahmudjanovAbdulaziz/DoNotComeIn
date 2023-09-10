from tkinter import *
from tkinter import messagebox
import random
import time


def click():
    # username = float(username_entry.get())
    # password = float(password_entry.get())
    # otv_finali = username / password
    username = username_entry.get()
    password = password_entry.get()
    if messagebox.askokcancel('Авторизация прошло успешна', f'Добро пожаловать {username}'):
        root_1.destroy()


root_1 = Tk()
root_1.title('Авторизация')
root_1.geometry('450x230')
root_1.resizable(width=False, height=False)
root_1['bg'] = 'black'

main_label = Label(root_1, text='Авторизация', font='Arial 15 bold', bg='black', fg='white')
main_label.pack()

username_label = Label(root_1, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
username_label.pack()

username_entry = Entry(root_1, bg='black', fg='lime', font='Arial 12')
username_entry.pack()

password_label = Label(root_1, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root_1, bg='black', fg='lime', font='Arial 12')
password_entry.pack()

send_btn = Button(root_1, text='Войти', command=click)
send_btn.pack(padx=10, pady=8)

root_1.mainloop()

root = Tk()
root.title('Выбор игры')
root.geometry('820x620')
root.resizable(width=False, height=False)
root['bg'] = 'orange'

colors = ['red', 'orange', 'lime', 'blue']
count = 0


def bal():
    bal_1.delete(ALL)
    x = random.randint(10, 580)
    y = random.randint(10, 580)
    r = 30
    new_ball = bal_1.create_oval(x, y, x + r, x + r, fill=random.choice(colors), width=0)
    bal_1.tag_bind(new_ball, '<Button-1>', click_on_circle())
    root.after(1500, bal)


def click_on_circle():
    global count
    count = count + 1
    print(str(count))
    p.delete(ALL)
    p.create_text(80, 30, font='Arial 18', text='Попаданий: ')
    p.create_text(180, 30, font='Arial 20', text=str(count))


def give_ball():
    btn_1.pack_forget()
    btn_2.pack_forget()
    btn_4.pack_forget()
    btn_5.pack_forget()
    bal_1.pack()

    root.title('Поймай Шарик')
    bal()
    p.pack()
    root.geometry('600x600')


def see_war_game():
    tk = Tk()
    app_running = True

    size_canvas_x = 500
    size_canvas_y = 500
    s_x = s_y = 8  # размер игрового поля
    s_y = 8
    step_x = size_canvas_x // s_x  # шаг по горизонтали
    step_y = size_canvas_y // s_y  # шаг по вертикали
    size_canvas_x = step_x * s_x
    size_canvas_y = step_y * s_y
    delta_menu_x = 4
    menu_x = step_x * delta_menu_x  # 250
    menu_y = 40
    ships = s_x // 2  # определяем максимальное кол-во кораблей
    ship_len1 = s_x // 5  # длина первого типа корабля
    ship_len2 = s_x // 3  # длина второго типа корабля
    ship_len3 = s_x // 2  # длина третьего типа корабля
    enemy_ships1 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
    enemy_ships2 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
    list_ids = []  # список объектов canvas

    # points1 - список куда мы кликнули мышкой
    points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
    points2 = [[-1 for i in range(s_x)] for i in range(s_y)]

    # boom - список попаданий по кораблям противника
    boom = [[0 for i in range(s_x)] for i in range(s_y)]

    # ships_list - список кораблей игрока 1 и игрока 2
    ships_list = []

    # print(enemy_ships1)

    def on_closing():
        global app_running
        if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
            app_running = False
            tk.destroy()

    tk.protocol("WM_DELETE_WINDOW", on_closing)
    tk.title("Игра Морской Бой")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=size_canvas_x + menu_x + size_canvas_x, height=size_canvas_y + menu_y, bd=0,
                    highlightthickness=0)
    canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
    canvas.create_rectangle(size_canvas_x + menu_x, 0, size_canvas_x + menu_x + size_canvas_x, size_canvas_y,
                            fill="lightyellow")
    canvas.pack()
    tk.update()

    def draw_table(offset_x=0):
        for i in range(0, s_x + 1):
            canvas.create_line(offset_x + step_x * i, 0, offset_x + step_x * i, size_canvas_y)
        for i in range(0, s_y + 1):
            canvas.create_line(offset_x, step_y * i, offset_x + size_canvas_x, step_y * i)

    draw_table()
    draw_table(size_canvas_x + menu_x)

    t0 = Label(tk, text="Игрок №1", font=("Helvetica", 16))
    t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
    t1 = Label(tk, text="Игрок №2", font=("Helvetica", 16))
    t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)

    t0.configure(bg="red")
    t0.configure(bg="#f0f0f0")

    def button_show_enemy1():
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships1[j][i] > 0:
                    color = "red"
                    if points1[j][i] != -1:
                        color = "green"
                    _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                                  fill=color)
                    list_ids.append(_id)

    def button_show_enemy2():
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships2[j][i] > 0:
                    color = "red"
                    if points2[j][i] != -1:
                        color = "green"
                    _id = canvas.create_rectangle(size_canvas_x + menu_x + i * step_x, j * step_y,
                                                  size_canvas_x + menu_x + i * step_x + step_x, j * step_y + step_y,
                                                  fill=color)
                    list_ids.append(_id)

    def button_begin_again():
        global list_ids
        global points1, points2
        global boom
        global enemy_ships1, enemy_ships2
        for el in list_ids:
            canvas.delete(el)
        list_ids = []
        generate_ships_list()
        # print(ships_list)
        enemy_ships1 = generate_enemy_ships()
        enemy_ships2 = generate_enemy_ships()
        points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
        points2 = [[-1 for i in range(s_x)] for i in range(s_y)]
        boom = [[0 for i in range(s_x)] for i in range(s_y)]

    b0 = Button(tk, text="№1", command=button_show_enemy1, width=2, height=1)
    b0.place(x=size_canvas_x + 20, y=30)

    b1 = Button(tk, text="№2", command=button_show_enemy2, width=2, height=1)
    b1.place(x=size_canvas_x + 20, y=70)

    b2 = Button(tk, text="Начать заново!", command=button_begin_again)
    b2.place(x=size_canvas_x + 20, y=110)

    def draw_point(x, y):
        # print(enemy_ships1[y][x])
        if enemy_ships1[y][x] == 0:
            color = "red"
            id1 = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
            id2 = canvas.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3,
                                     x * step_x + step_x - step_x // 3,
                                     y * step_y + step_y - step_y // 3, fill="white")
            list_ids.append(id1)
            list_ids.append(id2)
        if enemy_ships1[y][x] > 0:
            color = "blue"
            id1 = canvas.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,
                                          y * step_y + step_y // 2 + step_y // 10, fill=color)
            id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                          x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
            list_ids.append(id1)
            list_ids.append(id2)

    def draw_point2(x, y, offset_x=size_canvas_x + menu_x):
        # print(enemy_ships1[y][x])
        if enemy_ships2[y][x] == 0:
            color = "red"
            id1 = canvas.create_oval(offset_x + x * step_x, y * step_y, offset_x + x * step_x + step_x,
                                     y * step_y + step_y,
                                     fill=color)
            id2 = canvas.create_oval(offset_x + x * step_x + step_x // 3, y * step_y + step_y // 3,
                                     offset_x + x * step_x + step_x - step_x // 3,
                                     y * step_y + step_y - step_y // 3, fill="white")
            list_ids.append(id1)
            list_ids.append(id2)
        if enemy_ships2[y][x] > 0:
            color = "blue"
            id1 = canvas.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,
                                          offset_x + x * step_x + step_x,
                                          y * step_y + step_y // 2 + step_y // 10, fill=color)
            id2 = canvas.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                          offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y,
                                          fill=color)
            list_ids.append(id1)
            list_ids.append(id2)

    def check_winner(x, y):
        win = False
        if enemy_ships1[y][x] > 0:
            boom[y][x] = enemy_ships1[y][x]
        sum_enemy_ships1 = sum(sum(i) for i in zip(*enemy_ships1))
        sum_boom = sum(sum(i) for i in zip(*boom))
        # print(sum_enemy_ships1, sum_boom)
        if sum_enemy_ships1 == sum_boom:
            win = True
        return win

    def check_winner2():
        win = True
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships1[j][i] > 0:
                    if points1[j][i] == -1:
                        win = False
        # print(win)
        return win

    def check_winner2_igrok_2():
        win = True
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships2[j][i] > 0:
                    if points2[j][i] == -1:
                        win = False
        # print(win)
        return win

    def add_to_all(event):
        global points1, points2
        _type = 0  # ЛКМ
        if event.num == 3:
            _type = 1  # ПКМ
        # print(_type)
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
        # print(mouse_x, mouse_y)
        ip_x = mouse_x // step_x
        ip_y = mouse_y // step_y
        #  print(ip_x, ip_y, "_type:", _type)

        # первое игровое поле
        if ip_x < s_x and ip_y < s_y:
            if points1[ip_y][ip_x] == -1:
                points1[ip_y][ip_x] = _type
                draw_point(ip_x, ip_y)
                # if check_winner(ip_x, ip_y):
                if check_winner2():
                    print("Победа Игрока №2 (Все корабли противника Игрока №1 подбиты)!!!!!")
                    points1 = [[10 for i in range(s_x)] for i in range(s_y)]
                    points2 = [[10 for i in range(s_x)] for i in range(s_y)]
            # print(len(list_ids))

        # второе игровое поле
        if ip_x >= s_x + delta_menu_x and ip_x <= s_x + s_x + delta_menu_x and ip_y < s_y:
            # print("ok")
            if points2[ip_y][ip_x - s_x - delta_menu_x] == -1:
                points2[ip_y][ip_x - s_x - delta_menu_x] = _type
                draw_point2(ip_x - s_x - delta_menu_x, ip_y)
                # if check_winner(ip_x, ip_y):
                if check_winner2_igrok_2():
                    print("Победа Игрока №1 (Все корабли противника Игрока №2 подбиты)!!!!!")
                    points1 = [[10 for i in range(s_x)] for i in range(s_y)]
                    points2 = [[10 for i in range(s_x)] for i in range(s_y)]

    canvas.bind_all("<Button-1>", add_to_all)  # ЛКМ
    canvas.bind_all("<Button-3>", add_to_all)  # ПКМ

    def generate_ships_list():
        global ships_list
        ships_list = []
        # генерируем список случайных длин кораблей
        for i in range(0, ships):
            ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
        # print(ships_list)

    def generate_enemy_ships():
        global ships_list
        enemy_ships = []

        # подсчет суммарной длины кораблей
        sum_1_all_ships = sum(ships_list)
        sum_1_enemy = 0

        # print("sum: ", sum_1_all_ships)

        while sum_1_enemy != sum_1_all_ships:
            # обнуляем массив кораблей врага
            enemy_ships = [[0 for i in range(s_x + 1)] for i in
                           range(
                               s_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

            for i in range(0, ships):
                len = ships_list[i]
                horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

                primerno_x = random.randrange(0, s_x)
                if primerno_x + len > s_x:
                    primerno_x = primerno_x - len

                primerno_y = random.randrange(0, s_y)
                if primerno_y + len > s_y:
                    primerno_y = primerno_y - len

                # print(horizont_vertikal, primerno_x,primerno_y)
                if horizont_vertikal == 1:
                    if primerno_x + len <= s_x:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                                   enemy_ships[primerno_y][primerno_x + j] + \
                                                   enemy_ships[primerno_y][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y + 1][primerno_x + j] + \
                                                   enemy_ships[primerno_y - 1][primerno_x + j]
                                # print(check_near_ships)
                                if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                    enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                            except Exception:
                                pass
                if horizont_vertikal == 2:
                    if primerno_y + len <= s_y:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                                   enemy_ships[primerno_y + j][primerno_x] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                                   enemy_ships[primerno_y + j][primerno_x + 1] + \
                                                   enemy_ships[primerno_y + j][primerno_x - 1]
                                # print(check_near_ships)
                                if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                    enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                            except Exception:
                                pass

            # делаем подсчет 1ц
            sum_1_enemy = 0
            for i in range(0, s_x):
                for j in range(0, s_y):
                    if enemy_ships[j][i] > 0:
                        sum_1_enemy = sum_1_enemy + 1

            # print(sum_1_enemy)
            # print(ships_list)
            # print(enemy_ships)
        return enemy_ships

    generate_ships_list()
    # print(ships_list)
    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    # print("**********")
    # print(enemy_ships1)
    # print("**********")
    # print(enemy_ships2)
    # print("**********")

    while app_running:
        if app_running:
            tk.update_idletasks()
            tk.update()
        time.sleep(0.005)


def snake_game():
    Game_Runner = True

    game_width = 500
    game_height = 500
    snake_item = 20
    snake_color1 = 'red'
    snake_color2 = 'yellow'

    virtual_game_x = game_width // snake_item
    virtual_game_y = game_height // snake_item

    snake_x = virtual_game_x // 2
    snake_y = virtual_game_y // 2
    snake_x_nav = 0
    snake_y_nav = 0

    snake_list = []
    snake_size = 5

    tk1 = Tk()
    tk1.title('Игра Змейка!!!')
    tk1.resizable(0, 0)
    tk1.wm_attributes('-topmost', 1)
    canvas = Canvas(tk1, width=game_width, height=game_height, bd=0, highlightthickness=0)
    canvas.pack()
    tk1.update()

    present_color1 = 'blue'
    present_color2 = 'lime'
    presents_list = []
    presents_size = 25
    for i in range(presents_size):
        x = random.randrange(virtual_game_x)
        y = random.randrange(virtual_game_y)
        id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                 y * snake_item + snake_item, fill=present_color1)
        id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                 y * snake_item + snake_item - 2, fill=present_color2)
        presents_list.append([x, y, id1, id2])
    print(presents_list)

    def snake_paint_item(canvas, x, y):
        global snake_list
        id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                      y * snake_item + snake_item, fill=snake_color2)
        id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                      y * snake_item + snake_item - 2, fill=snake_color2)
        snake_list.append([x, y, id1, id2])
        print(snake_list)

    snake_paint_item(canvas, snake_x, snake_y)

    def check_can_we_delete_snake_item():
        if len(snake_list) >= snake_size:
            temp_item = snake_list.pop(0)
            print(temp_item)
            canvas.delete(temp_item[2])
            canvas.delete(temp_item[3])

    def chek_if_we_fount_present():
        global snake_size
        for i in range(len(presents_list)):
            if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
                # print('found')
                snake_size = snake_size + 1
                canvas.delete(presents_list[i][2])
                canvas.delete(presents_list[i][3])

        # print(snake_x, snake_y)

    def snake_move(event):
        global snake_x
        global snake_y
        global snake_x_nav
        global snake_y_nav
        if event.keysym == 'Up':
            snake_x_nav = 0
            snake_y_nav = -1
            check_can_we_delete_snake_item()
        elif event.keysym == 'Down':
            snake_x_nav = 0
            snake_y_nav = 1
            check_can_we_delete_snake_item()
        elif event.keysym == 'Left':
            snake_x_nav = -1
            snake_y_nav = 0
            check_can_we_delete_snake_item()
        elif event.keysym == 'Right':
            snake_x_nav = 1
            snake_y_nav = 0
            check_can_we_delete_snake_item()
        snake_x = snake_x + snake_x_nav
        snake_y = snake_y + snake_y_nav
        snake_paint_item(canvas, snake_x, snake_y)
        chek_if_we_fount_present()

    canvas.bind_all("<KeyPress-Left>", snake_move)
    canvas.bind_all("<KeyPress-Right>", snake_move)
    canvas.bind_all("<KeyPress-Up>", snake_move)
    canvas.bind_all("<KeyPress-Down>", snake_move)

    def game_over():
        exit(1)

    def check_if_borders():
        if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
            game_over()

    def check_we_touch_self(f_x, f_y):
        global Game_Runner
        if not (snake_x_nav == 0 and snake_y_nav == 0):
            for i in range(len(snake_list)):
                if presents_list[i][0] == f_x and snake_list[i][1] == f_y:
                    print('found')
                Game_Runner = False

    while 1:
        check_can_we_delete_snake_item()
        chek_if_we_fount_present()
        check_if_borders()
        check_we_touch_self(snake_x + snake_x_nav, snake_y + snake_y_nav)
        snake_x = snake_x + snake_x_nav
        snake_y = snake_y + snake_y_nav
        snake_paint_item(canvas, snake_x, snake_y)
        tk1.update_idletasks()
        tk1.update()
        time.sleep(0.15)

    tk1.mainloop()


btn_1 = Button(root, text='Камень \nНожницы \nБумага', font='Arial 14', width=20, height=10)
btn_1.pack(padx=0, pady=0, anchor=SE)

btn_2 = Button(root, text='Виктарина', font='Arial 14', width=20, height=10, )
btn_2.place(x=0, y=0)
# btn_2.pack(padx=100, pady=0, anchor=NW,)


btn_4 = Button(root, text='Змейка', font='Arial 14', width=20, height=10, command=snake_game)
btn_4.pack(padx=0, pady=0, anchor=SE)

btn_5 = Button(root, text='Поймай шарик', font='Arial 14', width=20, height=10, command=give_ball)
btn_5.place(x=0, y=237)

bal_1 = Canvas(root, width=600, height=600, bg='white')
p = Canvas(root, width=600, height=100, bg='orange')

btn_see_war = Button(root, text='Морской бой', font='Arial 14', width=20, height=10, command=see_war_game)
btn_see_war.place(x=450, y=120, anchor=CENTER)

root.mainloop()
