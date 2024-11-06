def divide(a,b):
    return a/b
try:
    a = int(input('Podaj pierwsza liczbe: '))
    b = int(input('Podaj druga liczbe: '))
    print(divide(a,b))
except ZeroDivisionError:
    print('Nie mozna dzielic przez 0')
finally:
    print('To wykona sie zawsze')

print('Koniec programu')