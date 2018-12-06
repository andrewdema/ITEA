a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
result = 0
if a < b:
    for i in range(a, b + 1):
        if i >= 1:
            result = result + i
elif a > b:
    for i in range(b, a+1):
        if i >= 1:
            result = result + i

if result:
    print ('The sum of all positive integers from the smallest to the greater (inclusive): ',result)
else:
    print('There are no natural numbers in this range')


