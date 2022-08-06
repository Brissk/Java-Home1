# Задача : Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


# first_name = input('Введите ваше имя ')
# second_name = input('Введите вашу фаммлию ')
# phone_number = input('Введите ваш телефон ')
# description = input('Введите ваше описание ')
from operator import index


first_name = 'Дмитрий'
second_name = 'Кузнецов'
phone_number = '8953123456'
description = 'О прекрасный код'
def phone_book():
    my_format = input('В каком формате сохранять данные? Введите либо 1(в столбик), либо 2(в строчку)')
    if my_format == '1':
        while True:
            with open('Phone_book1.txt','a',encoding='utf-8') as data:
                data.write(f'Имя - {first_name} \n')
                data.write(f'Фамилия - {second_name} \n')
                data.write(f'Телефон - {phone_number} \n')
                data.write(f'Описание - {description} \n')
                choise = input('Добавить следующий контакт? y/n? ')
                if choise == 'y':
                    continue
                elif choise =='n':
                    break
    elif my_format == '2':
        while True:
            with open('Phone_book2.txt','a',encoding='utf-8') as data:
                data.write(f'Имя - {first_name}, ')
                data.write(f'Фамилия - {second_name}, ')
                data.write(f'Телефон - {phone_number}, ')
                data.write(f'Описание - {description} \n')
                choise = input('Добавить следующий контакт? y/n? ')
                if choise == 'y':
                    continue
                elif choise =='n':
                    break   
    else:
        print('Вы ввели не то число')
        phone_book()
    

phone_book()

# with open('Phone_book.txt','r',encoding='utf-8') as data: # Распечатать весь справочник
#     a = data.read()
#     print(a)


def user_book(): 
    telephone_book = \
        {
            'Имя': input('Введите имя '),
            'Фамилия': input('Введите фамилию '),
            'Телефон': input('Введите телефон '),
            'Комментарий': input('Введите комментарий ')
        }
    return telephone_book

