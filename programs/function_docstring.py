def print_max(x, y):
    '''Wypisuje maksymalną liczbę spośród dwóch podanych.

    Obydwie wartości muszą być liczbami całkowitymi.'''
    # Zmienia na liczby całkowite, jeżeli to możliwe.
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
