def logger_puple(string_puple):
    with open ('puple.csv', 'a', encoding='utf-8') as file:
        file.writelines(f'{string_puple}\n')
    print('Запись добавлена')