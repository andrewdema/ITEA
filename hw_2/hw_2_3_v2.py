'''уточнить задачу 2 - просят ввести натуральное число - это целые положительные числа, но упоминают что 0!=1. Вопрос - 0 учитывать?)'''

n = int(input('Enter a natural number: '))
result = 1
i = 0
while i < n:
     i += 1
     result = result * i

if n >= 0:
    print('{}! = {}'.format(n, result))
else:
    print('Enter a natural number! For example, 1, 2, 3, 4, 5, 6, 7, 8, 9 …')