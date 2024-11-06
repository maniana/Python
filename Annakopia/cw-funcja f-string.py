
def przedstaw_sie(imie, wiek):
    return f'Nazywasz się {imie} i masz {wiek} lat'

while True:
    imie = input('Jak się nazywasz: ')
    if imie.isalpha():  #petla w ktorej musi podac litery
        break
    print("Imię powinno zawierać tylko litery.")

while True:
    wiek = input('Ile masz lat: ')
    if wiek.isdigit():  #petla w ktorej musi podac cyfry
        break
    print("Wiek powinien być liczbą całkowitą.")

wynik = przedstaw_sie(imie, wiek)
print(wynik)