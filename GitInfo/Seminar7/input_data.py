def input_user():
    x = int(input('Введите число a: '))
    y = int(input('Введите число b: '))
    return x, y


def operation():
    user_oper = input('Введите операцию: ')
    return user_oper


def contin():
    n = input('Хотите продолжить? y/n ').lower()
    if n == 'n':
        return False
    return True