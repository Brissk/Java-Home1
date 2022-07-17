# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multiply(my_list:list):   
    result = 1
    if len(my_list)%2 == 0:
        for i in range(int(len(my_list)/2)):      
            result = my_list[i] * my_list[-1-i]
            print(result)
    else:
        for i in range(int(len(my_list)/2+1)):      
            result = my_list[i] * my_list[-1-i]
            print(result)
          
my_list = [2, 3, 5, 9, 3, 7]
multiply(my_list)