def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input('Podaj liczbe: '))

if is_even(number):
    print(f'Liczba {number} jest parzysta')
else:
   print(f'Liczba {number} jest nieparzysta')


