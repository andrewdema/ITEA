n = int(input('Enter a natural number: '))
print('Now we calculate the factorial of the entered number:')
result = 1
if n == 0 or n == 1:
    result

elif n > 1:
    for i in range(1, n+1):
        result = result * i

else:
    print('Enter a natural number! For example, 1, 2, 3, 4, 5, 6, 7, 8, 9 …')

if n >= 0:
    print('{}! = {}'.format(n, result))