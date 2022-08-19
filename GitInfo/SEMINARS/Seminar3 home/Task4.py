# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def ten_to_two(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2
    print(result)

ten_to_two(3)