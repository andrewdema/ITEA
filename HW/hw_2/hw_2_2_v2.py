# Ввести два числа и посчитать сколько между ними натуральных.
# Eсли введенные числа не целые, а вещественные, например, 2.2 и 5.8:

import math

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
result = 0

if a < b:
    for i in range(math.ceil(a), math.floor(b) + 1):  # можно не прибавлять единичку, если мы и для b тоже будем использовать метод ceil range(math.ceil(a), math.ceil(b))
        if i >= 1:
            result = result + i
elif a > b:
    for i in range(math.ceil(b), math.floor(a) + 1):
        if i >= 1:
            result = result + i

if result:
    print('The sum of all positive integers from the smallest to the greater (inclusive): ', result)
else:
    print('There are no natural numbers in this range')


