# Задача 1: Напишите программу которая принимает на вход число N, и выдаёт последовательность из N членов

def print_numbers(N):
    x = 1
    for i in range(N):
        print(x)
        x = x * -3
        

print_numbers(5)


    