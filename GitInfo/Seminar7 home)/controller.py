import input_data
import func
import output_data
import data_keeper


def button():
    
    match input_data.vibor():
        case 1:
            a = input_data.input_user()
            data_keeper.keeper(a)
        case 2:
            func.find_person()
        case 3:
            func.del_user()
        case 4:
            output_data.print_person()

    a = input('Хотите выполнить ещё какие-либо действия? y/n ')
    if a =='y':
        button()