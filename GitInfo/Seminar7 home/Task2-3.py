# Задача 2: Игра "Конфеты" с непобедимым компьютером

import random
rand = random.randint(0, 1)
start = input('Стартуем, когда нажмёте клавишу')
if rand == 0:
    print('Ходит игрок № 1')
else:
    print('Ходит игрок № 2')
x = 0
y = 165
z = y % 29
for i in range(50):
    print(f'Ход № {i+1}')
    if i == 0:
        b = z
        print(f'Компьютер вводит число {b}')
        x += b
        print(f'Общее число конфет = {x}')
        a = int(input('Ваше число '))
        x += a
        print(f'Общее число конфет = {x}')
    else:
        b = 29-a
        print(f'Компьютер вводит число {b}')
        x += b
        if x == y:
            print('Компьютер победил')
            break    
        print(f'Общее число конфет = {x}')
        a = int(input('Ваше число '))
        x += a
        if x == y:
            print('Вы победили')
            break
        elif x > y:
            while x > y:
                print(f'Число {x} больше чем нужно, введите другое число')
                x -= a
                a = int(input('Ваше число '))
                x += a
        if x == y:
            print('Игрок 1 победил')
            break
        print(f'Общее число конфет = {x}')
