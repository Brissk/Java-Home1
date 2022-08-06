import pandas as pd



def print_person():
    file = pd.read_csv('Phone_book.csv')
    file.index += 1
    print(file)
