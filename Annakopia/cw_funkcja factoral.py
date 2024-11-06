def factorial(n):
    if n < 0:
        return "Nie można obliczyć silni dla liczb ujemnych."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Podaj liczbe: '))
print(f'Silnia z {n} wynosi {factorial(n)}')