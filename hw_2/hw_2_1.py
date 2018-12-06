print('Hello! Let\'s solve the quadratic equation!\n')

a = float(input('Please enter the coefficient a = '))
if a != 0:
    b = float(input('Please enter the coefficient b = '))
    c = float(input('Please enter the coefficient c = '))
    print('Fine! Now we find the roots of the quadratic equation {}*x^2 + {}*x + {} = 0\n'.format(a, b, c))

    diskr = b ** 2 - 4 * a * c
    print('Discriminant = ', diskr)

    if diskr < 0:  # вывести копмлексные корни на экран
        from cmath import sqrt
        koren1 = (-b + sqrt(diskr)) / 2 * a
        koren2 = (-b - sqrt(diskr)) / 2 * a
        print('Since the discriminant is negative, the quadratic equation has no real roots, but, according to the theorem,\nit has two roots in the field of complex numbers:')
        print('first root: x1 = ', koren1)
        print('second root: x2 = ', koren2)

    elif diskr == 0:
        from math import sqrt
        koren = (-b + sqrt(diskr)) / 2 * a
        print('The discriminant is zero, so the equation has only one root: x = ', koren)

    elif diskr > 0:
        from math import sqrt
        koren1 = (-b + sqrt(diskr)) / 2 * a
        koren2 = (-b - sqrt(diskr)) / 2 * a
        print('The discriminant is greater than zero, so we have two roots:')
        print('first root: x1 = ', koren1)
        print('second root: x2 = ', koren2)
else:
    print('You violated the conditions of the theorem - the coefficient a can not be equal to zero!!!')
