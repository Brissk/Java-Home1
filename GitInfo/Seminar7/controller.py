import input_data
import func
import output_data
import data_keeper


def button():
    x, y = input_data.input_user()
    oper = input_data.operation()
    result = 0
    match oper:
        case '+':
            result = func.func_sum(x, y)
        case '-':
            result = func.func_sub(x, y)
        case '*':
            result = func.func_mult(x, y)
        case '/':
            result = func.func_div(x, y)
    output_data.output_user(result)
    data_keeper.logger(x, y, oper, result)
    return input_data.contin()