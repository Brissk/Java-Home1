# Задача 1: Вычислить число pi c заданной точностью d

import math

def pi_accurate(d):
    d = int(input('Сколько знаков после запятой '))
    print(f"{math.pi:.{d}f}")

pi_accurate(3)
    