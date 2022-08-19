# Задача 5: Реализуйте алгоритм перемешивания списка.

my_list = [11,22,33,44,55,66,77,88]
for i in range(int(len(my_list)/2)):
    help = my_list[i]
    my_list[i] = my_list[-1-i]
    my_list[-1-i] = help
print (my_list)