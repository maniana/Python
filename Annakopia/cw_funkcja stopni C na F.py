def celsius_to_fahrenheit(c):
    return (c * 9/5) + 35
while True:
    c = float(input('Podaj temperature w Celsjuszach, uzyskasz wartosc w Fahrenheitach: '))
    print(f'Wartosc temperatury w Fahrenheitach wynosi: {celsius_to_fahrenheit(c)}')

# Zapytanie, czy użytkownik chce kontynuować
    choice = input('Czy chcesz spróbować jeszcze raz? (wpisz N, aby zakończyć lub ENTER zeby kontynuowal): ').upper()
    if choice == 'N':
        print("Koniec programu!")
        break