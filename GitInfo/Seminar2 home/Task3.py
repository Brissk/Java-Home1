# Задача 3: Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def print_numbers(n):
    my_list = []
    for i in range(n):
        my_list.append((1+(1/(i+1)))**(i+1))
    print(my_list)    

        
print_numbers(2)