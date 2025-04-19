from prettytable import PrettyTable
from random import randint

table = PrettyTable()
number = randint(1, 100)


print('''
      Угадай число!
      Для победы угадай с 5 попыток
      За победу + 10 за поражение - 10
      ''')


def guess_the_number():
    '''Игра угадай число!'''

    count = 0
    balance = 100

    while True:
        menu = input('go для начала, no для выхода: ')
        if menu != 'go' and menu != 'no':
            print('Неверная команда')
            continue
        if menu == 'no':
            print('Приходи ещё!')
            break
        if menu == 'go':
            while True:
                guess = int(input('Введите целое число от 1 до 100 число: '))
                table.field_names = ['Попытка', 'Число', 'Результат']
                if guess < number:
                    count += 1
                    table.add_row([str(count), str(guess), 'Меньше'])
                    print('Ваше число меньше того, что загаданно.')
                if guess > number:
                    count += 1
                    table.add_row([str(count), str(guess), 'Больше'])
                    print('Ваше число больше того, что загаданно.')
                if guess == number:
                    count += 1
                    table.add_row([str(count), str(guess), 'БИНГО!!!'])
                    if count <= 5:
                        balance += 10
                    else:
                        balance -= 10
                    break
        print(
            'Отличная интуиция! Вы угадали число :)'
            'С ' + str(count) + ' попыток!')
        count = 0
        print(balance)
        print(table)

        if menu == 'no':
            break


guess_the_number()
