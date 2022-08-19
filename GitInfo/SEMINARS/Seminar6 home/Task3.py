# Задача 3: Найти сумму чисел списка стоящих на нечетной позиции

my_list = [1,2,3,4,5,6,7,8]
sum = 0
a = list(filter(lambda x:x%2==1,my_list))  #через lambda и filter
b = [i for i in my_list if i%2==1]         #второй вариант через list comp
for i in a:
    sum += i
# for i in b:
#     sum += i
print(sum)

