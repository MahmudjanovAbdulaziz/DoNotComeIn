def save_fizika():
    question = int(input('''\nЧто вы хотите узнать?
    1) Гармоническое колебание
    2)Круговая частота
    3)Частота 
    4)Связь круговой частоты с частотой
    '''))
    if question == 1:
        a = float(input('Амплитуда колебаний: '))
        w = float(input('циклическая чистота: '))
        t = float(input('Данный момент времени: '))
        p0 = float(input('Начальная фаза колебаний: '))
        x = a * ( w * t + p0 )
        print('\nРешение: ', a, '*', '(', w, '*', t, '+', p0, ')', '=', x)
        print('Ответ: ' ,x)
    elif question == 2:
        t = float(input('Период: '))
        p = 3.14
        w = (2*p)/t
        print('\nРешение: ', '2', '*',p, '/', t, '=', w )
        print('Ответ: ' ,w)
    elif question == 3:
        t = float(input('Время: '))
        v = t / 1
        print('Решение: ', t , '/', '1', '=', v)
        print('Ответ ', v)
    a = float(input('Амплитуда колебаний: '))
    w = float(input('Скалярная величина: '))
    t = float(input('Время: '))
    








while True:
    save_fizika()