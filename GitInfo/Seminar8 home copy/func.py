import pandas as pd

def find_puple():
    df = pd.read_csv('Puple.csv')
    find_by_name = input('Введите имя для поиска ')
    df.index += 1
    print(df.query('Имя == @find_by_name'))


def del_puple():
    del_name = input('Введите имя для удаления ')
    df = pd.read_csv('Puple.csv').query('Имя != @del_name')
    print(df)

def del_puple1():
    del_name = input('Введите имя для удаления ')
    df = pd.read_csv('Puple.csv')
    df = df.set_index('Имя')
    df.drop([del_name],axis=0,inplace=True)

