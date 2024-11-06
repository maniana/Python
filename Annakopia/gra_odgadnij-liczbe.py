#Gra - losowanie liczby 1-100, zapisze do zmiennej, uzytkownik ma odgadnac
# import random
#
# losowa_liczba = random.randint(1, 100)
# print(losowa_liczba)
import random
losowa_liczba = random.randrange(1,101)
while True:
    liczba = int(input('Podaj liczbe:'))
    if liczba < 1 or liczba > 100:
      print('Liczba musi być w zakresie od 1 do 100.')
      continue  # Pomija resztę pętli i wraca do początku
    elif liczba == losowa_liczba:
       print('Brawo, odgadles liczbe !!!'
          'BRAWO BRAWO BRAWO BRAWO')
       break
    elif liczba > losowa_liczba:
       print('Ta liczba jest wieksza od liczby wylosowanej')
    elif liczba < losowa_liczba:
        print('Ta liczba jest mniejsza od liczny wylosowanej')
    else:
        print('Podales niewlasciwe dane')

# import random

# Losowanie liczby
# losowa_liczba = random.randint(1, 100)

# # Pętla, która będzie działać, dopóki nie zgadniesz liczby
# while True:
#     # Pobranie liczby od użytkownika, zamiana na liczbę całkowitą
#     liczba = int(input('Podaj liczbę: '))  # Zmieniamy input na int, żeby porównać liczby
#
#     if liczba == losowa_liczba:  # Poprawiona składnia if
#         print('Brawo, odgadłeś liczbę !!!')
#         print('BRAWO BRAWO BRAWO BRAWO')
#         break  # Kończymy pętlę, jeśli liczba została odgadnięta
#     elif liczba < losowa_liczba:
#         print('Ta liczba jest mniejsza od liczby wylosowanej')
#     else:  # Nie musisz podawać elif dla liczba > losowa_liczba, można użyć else
#         print('Ta liczba jest większa od liczby wylosowanej')
