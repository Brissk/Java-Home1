# Задача 2: Игра "Конфеты" человек с человеком

import random
rand = random.randint(0,1)
start = input('Стартуем, когда нажмёте клавишу')
if rand == 0:
    print('Ходит игрок № 1')
else:    
    print('Ходит игрок № 2')
x = 0
y = 60
for i in range(50):
    print(f'Ход № {i+1}')
    a = int(input('Введите число '))
    x += a
    if x == y: print('Вы победили'); break
    elif x > y: 
        while x>y:
            print(f'Число {x} больше чем нужно, введите другое число')
            x -= a
            a = int(input('Введите число '))
            x += a
    if x == y: print('Вы победили'); break
    print(x)
    b = int(input('Введите число '))
    x += b
    if x == y: print('Вы победили'); break
    elif x > y: print('Вы проиграли'); break
    print(x)