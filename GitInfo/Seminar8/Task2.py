with open('Phone_book.csv','a',encoding='utf-8') as data:
    a = data.readlines()
    b = input('Введите имя для поиска ')
    for i in a:
        start = i.find(b)
        print(start)
        end = i.find('\n', index_start)
        print(i[index_start - 8:index_end - 1])
        break


def user_book(): 
    telephone_book = {'Имя': input('Введите имя '),'Фамилия': input('Введите фамилию '), 'Телефон': input('Введите телефон '),'Комментарий': input('Введите комментарий ') }
    return telephone_book