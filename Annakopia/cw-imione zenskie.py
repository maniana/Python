# name = input ("Program sprawdza czy imie jest meskie, czy zenskie. Wpisz imie:" )
# end = str(name[-1])
# if name =='a':
#     print("Jest to prawdopodobnie imie zenskie")
# else:
#     print("Jest to prawdopodobnie imie meskie")


name = input("Program sprawdza, czy imię jest męskie, czy żeńskie. Wpisz imię: ")

# Sprawdzamy, czy imię zawiera tylko litery
if name.isalpha():
    end = name[-1]  # Pobieramy ostatnią literę imienia
    if end == 'a':  # Sprawdzamy, czy ostatnia litera to 'a'
        print("Jest to imię żeńskie")
    else:
        print("Jest to imię męskie")
else:
    print("Imię powinno zawierać tylko litery. Spróbuj ponownie.")

