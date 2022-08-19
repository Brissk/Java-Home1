# Задача 1: Задайте список строк. Напишите программу, которая определит,
# присутствует ли в заданном списке некое число

my_list = ['asd12','12','asd','87']

def search_number(list1, num):
    for i in list1:
        if str(num) in i:
            print(i)

search_number(my_list,12)


    