# Задача 2: Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит что её нет

my_list = ['123','qwe','asd',123,'zxc','qwe','ertqwe']

def str_find(list1, str1): 
    x = 0
    index = 0
    for i in range(len(list1)):
        if list1[i] == str1:
            x+=1
            if x == 2:
                print(f'Второе вохожение на позиции {i}')
                break
    if x!=2:
        print('Нет второго вхождения')




str_find(my_list,'123')