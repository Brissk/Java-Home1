# Задача 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = [2, 3, 5, 9, 3]

def sum_numbers(list1:list):
    sum = 0
    for i in range(1,len(list1),2): 
        sum += list1[i]
    print(sum)
          

sum_numbers(my_list)

    