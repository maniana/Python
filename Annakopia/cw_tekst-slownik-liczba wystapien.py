tekst = input('Wpisz tekst, na podstawie ktorego przeanalizuje ile razy wystapilo kazde kolejne slowo: ')
slowo = tekst.split()
zliczanie_slow = {}

for p_slowo in slowo:
    if p_slowo in zliczanie_slow:
        zliczanie_slow[p_slowo] += 1
    else:
        zliczanie_slow[p_slowo] = 1

for slowo, liczba in zliczanie_slow.items():

    print (f'{slowo} powtorzylo sie: {liczba} razy')

