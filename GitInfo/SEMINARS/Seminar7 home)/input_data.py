def vibor():
    my_vibor = {1:'Добавить контакт', 2:'Поиск по имени', 3:'Удалить контакт' , 4:'Вывести всё'}

    for i,j in my_vibor.items():
        print(i,j)
    result = int(input('Введите номер '))
    return result


def input_user():
    first_name = input('Введите ваше имя ')
    second_name = input('Введите вашу фамилию ')
    phone_number = input('Введите ваш телефон ')
    description = input('Введите ваше описание ')
    all_info = f'{first_name},{second_name},{phone_number},{description}'
    return all_info


