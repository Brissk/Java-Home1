import input_data


def logger(a, b, c, d):
    result = ''
    result += str(a) + c + str(b) + '=' + str(d)
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{result}\n')