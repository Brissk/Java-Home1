# Задача 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fib(num):
    list1 = [1, 1]
    list2 = [1, -1]
    for i in range(2,num):
        list1.append(list1[i-2]+list1[i-1])
    for i in range(2,num):
        list2.append(list2[i-2]-list2[i-1])
    list2.reverse()
    print(f'{list2} 0 {list1}')

Fib(8)