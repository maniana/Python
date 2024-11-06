
try:
    number = input("Podaj liczbe ")

    number = number.replace(",",".") #python widzi tylko . jako liczba dziesietna
    number = float(number)  # kazda liczba
    if number < 0:
        print("Liczba jest mniejsza od 0")
    elif number > 0:
        print("Liczba jest wieksza od 0")
    else:
        print("Rowna 0")
except ValueError:
    print("Podales zle dane")