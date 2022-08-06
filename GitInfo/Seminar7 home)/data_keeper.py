def keeper(person):
    with open('Phone_book.csv','a',encoding='utf-8') as data:
        data.writelines(f'{person}\n')


