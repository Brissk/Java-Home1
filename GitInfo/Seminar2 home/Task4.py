# Задача 4: Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

def sequence(num):
    list = []
    i = num*-1
    while i <= num:
        list.append(i)
        i += 1
    return list
# def find_position(list):
#     position = input('Введите позиции элементов через пробел')
#     print(f'Произведение элементов на указанных позициях = {list[int(position[0])] * list[int(position[2])]}')


my_list = sequence(4)

with open('test.txt', 'w') as file:
indices = input('Введите числа через пробел')
indices = indices.split(' ')
for el in indices:
    file.write(f'{el}\n')

file = open('test.txt', 'r')
data = file.read()
list_of_rows = data.split()
file.close()
print(list_of_rows)

result = 1
for i in list_of_rows:
    result *= my_list[int(i)]

print(f'{my_list} -> {list_of_rows} -> {result}')
