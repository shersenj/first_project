from prettytable import PrettyTable
from random import randint

table = PrettyTable()
number = randint(1, 100)
count = 0

print('Угадай число от 1 до 100')

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
        break
print('Отличная интуиция! Вы угадали число :) С ' + str(count) + ' попыток!')
print(table)
