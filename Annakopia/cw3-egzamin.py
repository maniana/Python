try:
    number = input("Jaki otrzymales wynik na egzaminie ")

    number = number.replace(",", ".")  # python widzi tylko . jako liczba dziesietna
    number = float(number)  # kazda liczba

    if number < 60:
        print("Niestety, jest to 1")
    elif 60 <= number <= 69:
        print("Zaliczone, dostajesz 2")
    elif 70 <= number <= 79:
        print("Dostajesz 3")
    elif 80 <= number <= 89:
        print("Dostajesz 4")
    elif 90 <= number <= 100:
        print("Dostajesz 5")
    else:
        print("Zla liczbe podales")
except ValueError:
    print("Podales zle dane")