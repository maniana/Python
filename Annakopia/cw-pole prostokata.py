try:
   print ("Program liczy pole prostokata, podaj dlugosc bokow a i b w cm")
   a = float(input("Podaj dlugosc boku a: "))
   b = float(input("Podaj dlugosc boku b: "))
   c = a * b
   print("Pole prostokata wynosi: ", c,"cm")
except ValueError:
   print ("Podales zle dane")

