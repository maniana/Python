def is_palidrome(s):
    if s[::-1] == s:
       return 'To slowo/liczba jest palidromem'
    else:
       return 'To slowo nie jest palidromem'
# Pętla, która działa, dopóki użytkownik nie wpisze 'N'
while True:
    a = input('Wpisz słowo, sprawdzę czy jest palindromem: ')
    print(is_palidrome(a))

# Zapytanie, czy użytkownik chce kontynuować
    choice = input('Czy chcesz spróbować jeszcze raz? (wpisz N, aby zakończyć lub ENTER zeby kontynuowal): ').upper()

    if choice == 'N':
      print("Koniec programu!")
      break
