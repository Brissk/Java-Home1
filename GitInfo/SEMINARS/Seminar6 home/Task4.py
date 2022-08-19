# Задача 4: Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = 6

list_of_keys = []
for i in range(n):
    list_of_keys.append(i+1)

list_of_values = []
for i in range(n):
    list_of_values.append(3*(i+1)+1)

my_dict = dict(zip(list_of_keys,list_of_values)) # через zip
print(my_dict)