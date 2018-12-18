# from calc import add,sub,mul,divi,expon
from calc import *

# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def divi(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         return e

def expon(a, b):
    return a ** b

loop = False
while loop == False:

    calculator = {'+':add, '-':sub, '*':mul, '/':divi, '**':expon} #ссылку на функцию помещаем, а не саму функцию!

    while True:
        try:
            x = float(input('Enter the first number: '))
            oper = input('Enter the operation of the proposed: '+str(list(calculator.keys()))+': ')
            y = float(input('Enter the second number: '))
        except ValueError:
            print('Please enter a number!')
        else:
            break

    result = None

    if oper in list(calculator.keys()):
        result = calculator[oper](x,y)  # calculator[oper] обращаемся к значению словаря по заданному ключу и вызываем ф-ию def
    else:
        print('Please enter the operation of the proposed!')

    try:
        if result is not None:
            print(result)
    except Exception as e:
        print(e)

    #exit_continue = None
    #while exit_continue not in ['y', 'n']:
    exit_continue = input('\nWant to continue? (Y/N): ').lower()
    if exit_continue.lower() == 'y':
        loop = False
    else:
        loop = True
        print('Work completed!')


# if result is not None:
#     print(result)
# else:
#     print('None a number')