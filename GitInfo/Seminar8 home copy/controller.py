import input_data
import logger
import output_data
import func


def button():
    match input_data.choice():
        case 1:
            a = input_data.input_puple()
            logger.logger_puple(a)
        case 2:
            func.find_puple()
        case 3:
            func.del_puple()
        case 4:
            output_data.print_puple()

    a = input('Хотите выполнить ещё какие-либо действия? y/n ')
    if a =='y':
        button()