# Задача 1: Доделать реализацию функции eval со скобками

def calc(s):
    count = ''
    digit = []
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
            if i == len(s)-1:
                digit.append(int(count))
        elif s[i] == '(': 
            digit.append(s[i])
        elif s[i] == ')': 
            digit.append(int(count))
            digit.append(s[i])
        elif s[i-1] == ')': 
            digit.append(s[i])
            count = ''
        else:
            digit.append(int(count))
            digit.append(s[i])            
            count = ''            
    return digit

def decision(my_list):
    my_list2 = []
    res = 1
    while len(my_list) > 1:
        if '(' in my_list:
            j = my_list.index('(')
            i = my_list.index(')')
            for k in range(j+1,i):
                my_list2.append(my_list[j+1]) 
                my_list.pop(j+1)   
            while len(my_list2) > 1:  
                if '/' in my_list2:
                    i = my_list2.index('/')
                    res = my_list2[i-1] / my_list2[i+1]
                    my_list2[i-1] = res
                    my_list2.pop(i+1)
                    my_list2.pop(i)
                elif '*' in my_list2:
                    i = my_list2.index('*')
                    res = my_list2[i-1] * my_list2[i+1]
                    my_list2[i-1] = res
                    my_list2.pop(i+1)
                    my_list2.pop(i)
                elif '-' in my_list2:
                    i = my_list2.index('-')
                    res = my_list2[i-1] - my_list2[i+1]
                    my_list2[i-1] = res
                    my_list2.pop(i+1)
                    my_list2.pop(i)
                elif '+' in my_list2:
                    i = my_list2.index('+')
                    res = my_list2[i-1] + my_list2[i+1]
                    my_list2[i-1] = res
                    my_list2.pop(i+1)
                    my_list2.pop(i)
            my_list[j] = my_list2[0]
            my_list.pop(j+1)
            my_list2 = []
        elif '/' in my_list:
            i = my_list.index('/')
            res = my_list[i-1] / my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '*' in my_list:
            i = my_list.index('*')
            res = my_list[i-1] * my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '-' in my_list:
            i = my_list.index('-')
            res = my_list[i-1] - my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '+' in my_list:
            i = my_list.index('+')
            res = my_list[i-1] + my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
    return res

s = '(1+5)/9+3*(8*7+10-5*5)*(5+5)+5-7+3*(10-1000)/2*5/9-3+4'
ss = '3*3/7*3/9+3/3/3*3*3/3*5/7'
sss = '6/5/4*7*5/8'
print(decision(calc(sss)))
print(eval(sss))