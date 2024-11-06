#Pobierz 3 liczby calkowite i uporzadkuj od najmniejszej do najwiekszej
try:
   liczba1 = int(input('Podaj pierwsza liczbe: '))
   liczba2 = int(input('Podaj druga liczbe: '))
   liczba3 = int(input('Podaj trzecia liczbe: '))
   liczby = [liczba1, liczba2, liczba3]
   liczby.sort()
   print(liczby)
except ValueError:
   print("Podales zle dane")

