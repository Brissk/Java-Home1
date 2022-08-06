# Задача 4:Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from unicodedata import digit

def compress(string):
    count = 1
    result = ''
    for i in range(len(string)-1): 
        if string[i] == string[i+1]:
            count += 1
            if i == len(string)-2:
                result += str(count) + string[i]
        elif string[i] != string[i+1]:
            result += str(count) + string[i]
            count = 1         
    return result

string = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

with open('file.txt', 'a') as data:
    data.write('Enter data ' + string + '\n')

print(compress(string))

with open('file.txt', 'a') as data:
    data.write('Exit data ' + compress(string) + '\n')

def decompress(string):
    count = 0
    result = ''
    list_of_nums = []
    list_of_symbols = []
    for i in range(len(string)): 
        if string[i].isdigit():
            result += string[i]
            if string[i+1].isdigit():
                continue            
            list_of_nums.append(result)
            result = ''
        else:
            list_of_symbols.append(string[i])
    for i in range(len(list_of_nums)):  
        list_of_nums[i] = int(list_of_nums[i])
    for i in range(len(list_of_nums)): 
        while list_of_nums[i] > count:
            result += list_of_symbols[i]
            count += 1
        count = 0
    return result

string2 = '9W3B24W1B14W'

with open('file2.txt', 'a') as data2:
    data2.write('Enter data ' + string2 + '\n')

print(decompress(string2))

with open('file2.txt', 'a') as data2:
    data2.write('Exit data ' + decompress(string2) + '\n')