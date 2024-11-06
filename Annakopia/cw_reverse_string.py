#przyjmuje reverse_string(s) ktora ptrzjmuje tekst i zwraca go w odwrotnej kolejnosci
def reverse_string(s):
    return s[::-1]

s = input('Wprowadz tekst, ktory zostanie wyswietlony w odwrotnej kolejnosci: ')
print(f'Tekst w odwrotnej kolejnosci to: {reverse_string(s)}')