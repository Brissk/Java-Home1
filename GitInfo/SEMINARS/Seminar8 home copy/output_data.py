import pandas as pd



def print_puple():
    file = pd.read_csv('Puple.csv')
    file.index += 1
    print(file)
