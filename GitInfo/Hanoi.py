def Hanoi(n, A, B, C):
    if n != 0:
        Hanoi(n - 1, A, C, B)
        print ('Move the plate from', A, 'to', B)
        Hanoi(n - 1, C, B, A)


def fact(n):
    if(n==1): return 1
    return n * fact(n-1)


print(fact(5))