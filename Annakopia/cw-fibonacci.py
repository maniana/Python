def fibonacci(n):
    if not isinstance(n,int):
        return 'Podaj liczbe calkowita'
    elif n < 1:
        return ('Liczba musi byc wieksza lub rowna 1: ')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

try:
    n = int(input('Podaj, ktora liczbe Fibonnaciego chcesz otrzymac: '))
    result = fibonacci(n)
    print(f'{n}-ta liczba Fibanacciego to:{fibonacci(n)}')
except ValueError:
    print('Podaj poprawna liczbe calkowita.')