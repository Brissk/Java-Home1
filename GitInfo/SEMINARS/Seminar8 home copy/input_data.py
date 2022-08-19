def input_puple():
    first_name = input('Введите ваше имя ')
    second_name = input('Введите вашу фамилию ')
    birthday = input('Введите ваш день рождения ')
    place = input('Введите ваше место ')
    phone_number = input('Введите ваш телефон ')
    status = input('Введите ваш статус ')
    all_info = f'{first_name},{second_name},{birthday},{place},{phone_number},{status}'
    return all_info

def choice():
    my_vibor = {1:'Добавить запись об ученике', 2:'Поиск по имени', 3:'Удалить запись об ученике' , 4:'Вывести полный список учеников'}

    for i,j in my_vibor.items():
        print(i,j)
    result = int(input('Введите номер '))
    return result