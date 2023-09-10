import schedule
import requests

def greeting():
    todos_dict = {
        '08:00' : 'Drink coffe',
        '11:00' : 'Work in phon',
        '23:59': 'hack my telephon'
    }
    print('Days tasks')
    for d, k in todos_dict.items():
        print(f'{d} - {k}')

    respons = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = respons.json()
    btc_price=f"BTC : {round(data.get('btc_usd').get('last'), 2)}$"
    print(btc_price)


def main():
    #schedule.every(3).seconds.do(greeting)
    schedule.every().day.at('21:05').do(greeting)


    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()

