# Задача 1: Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 

def calc(s):
    count = ''
    digit = []
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
        else:
            digit.append(int(count))
            digit.append(s[i])
            count = ''
    digit.append(int(count))
    return digit

def decision(my_list):
    while len(my_list) > 1:
        if '*' in my_list:
            i = my_list.index('*')
            res = my_list[i-1] * my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '/' in my_list:
            i = my_list.index('/')
            res = my_list[i-1] / my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '+' in my_list:
            i = my_list.index('+')
            res = my_list[i-1] + my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '-' in my_list:
            i = my_list.index('-')
            res = my_list[i-1] - my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
    return res
s = '24/3-5*3-3'
my_list = calc(s)
print(calc(s))
print(decision(my_list))




    