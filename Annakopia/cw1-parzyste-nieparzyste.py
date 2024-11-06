# Program,ktory sprawdza czy liczba jest parzysta czy nieparzysta

#
# print(c%2==0) #czy jest liczba parzysta
# print(not c%2==0)

try:
    number = input("Podaj liczbe ")

    number = int(number)
    if number % 2 == 0:
        print("Liczba parzysta")
    elif number % 2 != 0:
        print("Liczba nieparzysta")
    else:
        print("Podales zle dane")
except ValueError:
    print("Podales zle dane")


# Lepsza wersja programu:

try:
    number = input("Podaj liczbe ")

    number = int(number)  # Konwersja na liczbę całkowitą
    if number % 2 == 0:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
except ValueError:
    print("Podane zostaly zle dane")