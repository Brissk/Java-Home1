# Задача 3: Создайте программу для игры в ""Крестики-нолики"".

lis = [1,2,3,4,5,6,7,8,9]

def func_print(my_list):
    for i in range(3):
        for j in range(3):
            if i == 0:
                print(my_list[j], end=' ')
            if i == 1:
                print(my_list[j+3], end=' ')
            if i == 2:
                print(my_list[j+6], end=' ')
        print()
print('\033[37m\033[1m',end='')
func_print(lis)
for i in range(5):
    iks = None    
    iks = int(input(f'\033[32m\033[1m\033[3m{"Введите число, на место которого хотите поставить крестик "}\033[0m'))
    if iks in lis:
        i = lis.index(iks)
        lis[i] = '\033[31m\033[1m''X''\033[0m'
    print('\033[37m\033[1m',end='')
    func_print(lis)
        
    if lis[0] == '\033[31m\033[1m''X''\033[0m' and lis[1] == '\033[31m\033[1m''X''\033[0m' and lis[2] == '\033[31m\033[1m''X''\033[0m' or lis[3] == '\033[31m\033[1m''X''\033[0m' and lis[4] == '\033[31m\033[1m''X''\033[0m' and lis[5] == '\033[31m\033[1m''X''\033[0m' or lis[6] == '\033[31m\033[1m''X''\033[0m' and lis[7] == '\033[31m\033[1m''X''\033[0m' and lis[8] == '\033[31m\033[1m''X''\033[0m' or lis[0] == '\033[31m\033[1m''X''\033[0m' and lis[4] == '\033[31m\033[1m''X''\033[0m' and lis[8] == '\033[31m\033[1m''X''\033[0m' or lis[6] == '\033[31m\033[1m''X''\033[0m' and lis[4] == '\033[31m\033[1m''X''\033[0m' and lis[2] == '\033[31m\033[1m''X''\033[0m' or lis[0] == '\033[31m\033[1m''X''\033[0m' and lis[3] == '\033[31m\033[1m''X''\033[0m' and lis[6] == '\033[31m\033[1m''X''\033[0m' or lis[1] == '\033[31m\033[1m''X''\033[0m' and lis[4] == '\033[31m\033[1m''X''\033[0m' and lis[7] == '\033[31m\033[1m''X''\033[0m' or lis[2] == '\033[31m\033[1m''X''\033[0m' and lis[5] == '\033[31m\033[1m''X''\033[0m' and lis[8] == '\033[31m\033[1m''X''\033[0m': 
        print(f'\033[30m\033[41m{"Игра окончена. Победили Иксы!"}\033[0m')
        break     
    nol = None   
    nol = int(input(f'\033[32m\033[1m\033[3m{"Введите число, на место которого хотите поставить нолик "}\033[0m'))
    if nol in lis:
        i = lis.index(nol)
        lis[i] = '\033[33m\033[1m''0''\033[0m'
    print('\033[37m\033[1m',end='')
    func_print(lis)
    if lis[0] == '\033[33m\033[1m''0''\033[0m' and lis[1] == '\033[33m\033[1m''0''\033[0m' and lis[2] == '\033[33m\033[1m''0''\033[0m' or lis[3] == '\033[33m\033[1m''0''\033[0m' and lis[4] == '\033[33m\033[1m''0''\033[0m' and lis[5] == '\033[33m\033[1m''0''\033[0m' or lis[6] == '\033[33m\033[1m''0''\033[0m' and lis[7] == '\033[33m\033[1m''0''\033[0m' and lis[8] == '\033[33m\033[1m''0''\033[0m' or lis[0] == '\033[33m\033[1m''0''\033[0m' and lis[4] == '\033[33m\033[1m''0''\033[0m' and lis[8] == '\033[33m\033[1m''0''\033[0m' or lis[6] == '\033[33m\033[1m''0''\033[0m' and lis[4] == '\033[33m\033[1m''0''\033[0m' and lis[2] == '\033[33m\033[1m''0''\033[0m' or lis[0] == '\033[33m\033[1m''0''\033[0m' and lis[3] == '\033[33m\033[1m''0''\033[0m' and lis[6] == '\033[33m\033[1m''0''\033[0m' or lis[1] == '\033[33m\033[1m''0''\033[0m' and lis[4] == '\033[33m\033[1m''0''\033[0m' and lis[7] == '\033[33m\033[1m''0''\033[0m' or lis[2] == '\033[33m\033[1m''0''\033[0m' and lis[5] == '\033[33m\033[1m''0''\033[0m' and lis[8] == '\033[33m\033[1m''0''\033[0m': 
        print(f'\033[30m\033[43m{"Игра окончена. Победили Ноли!"}\033[0m')
        break    

# import tkinter.font as font

# #create Font object
# myFont = font.Font(family='Helvetica')

# button = Button(parent, font=myFont)
