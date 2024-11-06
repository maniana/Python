names = {'Mirek', 'Zbyszek', 'Zosia','Kasia', 'Wojtek'}  #set { nie pozwala na duplikaty
names2 = {'Zosia', 'Maciek', 'Krysia', 'Zbyszek'}

#suma
print(names | names2)
#albo
print(names.union(names2))

#czesc wspolna
print(names.intersection(names2))
print (names & names2)

#roznica
print(names.difference(names2))
print(names - names2)

#symetryczna roznica
print(names.symmetric_difference(names2))
print(names ^ names2)

# names.add('Kaziu')
# names.remove('Ziutek')
# print(names)

# for name in names:
#  print(name)
#
# names.update(['Bizia', 'Cizia'])
# print(names)