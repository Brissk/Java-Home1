# Задача 3: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def diff_min_max(my_list:list):
    my_list1 = []
    for i in range(len(my_list)):
        my_list1.append((int(my_list[i]*100)%100))
    
    print(max(my_list1) - min(my_list1))    

my_list = [1.1, 1.2, 3.1, 5.02, 10.01]  
diff_min_max(my_list)