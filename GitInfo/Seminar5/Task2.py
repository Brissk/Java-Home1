# Задача 2: Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.


a = [1, 5, 2, 3, 4, 6, 1, 7]


def func(num):
    my_list = []
    my_list.append(a[num])
    for i in range(num, len(a)):
        if a[i] > my_list[-1]:
            my_list.append(a[i])
    print(my_list)


for i in range(len(a)):
    func(i)



index = 0

# for n in range(1,len(list_input)):
#     for i,item in enumerate(list_input[:-n]):
#         new_list = [list_input[i]]
#         for j,item_2 in enumerate(list_input[i+n:]):
#             if item_2 > max_in_list(new_list):
#                 new_list.append(item_2)
#         if new_list not in new_list_dic.values():
#             new_list_dic[index] = new_list
#             index += 1

# print(new_list_dic)

def max_in_list(list_of_numbers):
    max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max:
            max = i
    return max

new_list_dic = {}

index = 0

for n in range(1,len(list_input)):
    for i,item in enumerate(list_input[:-n]):
        new_list = [list_input[i]]
        for j,item_2 in enumerate(list_input[i+n:]):
            if item_2 > max_in_list(new_list):
                new_list.append(item_2)

            
        if new_list not in new_list_dic.values():
            new_list_dic[index] = new_list
            index += 1

for i in new_list_dic:
    print(f"{i} : \t{new_list_dic[i]}")
