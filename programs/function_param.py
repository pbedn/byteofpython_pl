def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# wpisz zmienne bezpośrednio
print_max(3, 4)

x = 5
y = 7

# wpisz zmienne jako argumenty
print_max(x, y)
