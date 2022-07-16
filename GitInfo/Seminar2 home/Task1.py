# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def numbers(num):
    str1 = str(num)
    sum = 0
    for i in str1:
        if i == '.':
            continue
        sum += int(i)
    print(sum)
          

numbers(6782)

    