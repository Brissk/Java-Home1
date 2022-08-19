import pandas as pd

def find_person():
    with open('Phone_book.csv','r',encoding='utf-8') as data: 
        a = data.readlines()
        find_name = input('Введите имя для поиска ')
        for i in a:
            if i == find_name:
                print(i)
                break


def del_user():
    file = pd.read_csv('Phone_book.csv')
    del_name = input('Введите имя для удаления ')
    index = file.find(del_name)
    file.drop(index)
      
        

