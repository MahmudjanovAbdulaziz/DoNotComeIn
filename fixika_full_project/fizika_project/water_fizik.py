def water_fizik():
    try:
        questions = float(input('''\nЧто вы хотите узнать?
    1) Плотность житкости
    2) Плотность идеальных газов
    '''))

        if questions == 1:
            m = float(input('Масса: '  'кг '))
            w = float(input('Обьем: ' 'm^3 '))
            p = m / w
            print('Решение: ' , m , ' кг /' , w , ' m^3 =' , p )
            print('\nОтвет: ', p)
        elif questions == 2:
            p = float(input('Давление: '))
            m = float(input('Молярная масса: '))
            r = float(input('Газовая пастоянаня: '))
            t = float(input('Газовая пастоянная: '))
            po = p * m / r * t
            print("Решение: ", p ,'*', m, '/', r, '*', t, '=', po)
            print('\nОтвет: ', po)
    except ValueError:
        print('\nОшибка идентификации!!! Повторите снова!!!')


while True:
    water_fizik()
