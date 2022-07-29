# Задача 2: Игра "Конфеты" с глупым компьютером

import random
rand = random.randint(0,1)
start = input('Стартуем, когда нажмёте клавишу')
if rand == 0:
    print('Ходит игрок № 1')
else:    
    print('Ходит игрок № 2')
x = 0
for i in range(50):
    print(f'Ход № {i+1}')
    a = int(input('Введите число '))
    x += a
    if x == 285: print('Вы победили'); break
    elif x > 285: 
        while x>285:
            print(f'Число {x} больше чем нужно, введите другое число')
            x -= a
            a = int(input('Введите число '))
            x += a
    if x == 285: print('Игрок 1 победил'); break
    print(x)
    b = random.randint(1,29)
    print(f'Введите число {b}')
    print(b)
    x += b
    if x == 285: print('Вы победили'); break
    elif x > 285: 
        while x>285:
            print(f'Число {x} больше чем нужно, введите другое число')
            x -= b
            b = random.randint(1,29)
            x += b
    if x == 285: print('Игрок 2 победил'); break
    print(x)