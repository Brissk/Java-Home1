# Задача 1: Записать в файл все числа от 0 до числа заданного пользователем

a = int(input('Введите число '))

    
with open('test.txt','a',encoding='utf-8') as file:
    for i in range(a+1):
        #file.write(f'{i}\n')
        file.writelines('%s\n' % i)




    