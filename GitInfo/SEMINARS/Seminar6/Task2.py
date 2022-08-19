# Задача 2: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

def find_uniq(my_list: list) -> list:
    new_list = []
    for i in my_list:
        if i in my_list[i:]:
            continue
        else:
            new_list.append(i)
    return new_list


my_list = [1, 2, 3, 5, 1, 5, 3, 10] 
print('Изначальный список:', my_list)
print('Итоговый список', find_uniq(my_list))

def nonRepeatingElements(list):
    outputList = []
    for i in range(0, len(list)):
        if i == 0:
            if not (list[i] in list[i + 1 :]):
                outputList.append(list[i])
        elif i == len(list) - 1:
            if not (list[i] in list[:i]):
                outputList.append(list[i])
        else:
            if not ((list[i] in list[:i]) or (list[i] in list[i + 1 :])):
                outputList.append(list[i])
    return outputList


list = [1, 3, 8, 20, 15, 20, 8, 1]
print(f"Список неповторяющихся чисел последовательности {list} -> {nonRepeatingElements(list)}")
