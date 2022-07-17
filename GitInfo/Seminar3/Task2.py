# Задача 1: Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую.

def str_quantity(st1:str, st2:str): 
    t=0
    for i in range(len(st1)-len(st2)):
        if st1[i:i+len(st2)] == st2:
            t+=1
    print(t)


def find_str(base_string, symbol):
    position = 0
    qty = 0
    while True:
        position = base_string.find(symbol,position)
        if position == -1:
            break
        else:
            position += 1
            qty += 1
    print(qty)

find_str("d;sfljg;lskdfooooooo", "oo")