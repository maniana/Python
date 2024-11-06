phone_book = {'Kamil': 497284598345, 'Konrad': 542598496, 'Jerzy': 935846767, 'Anna': 7675777}

print(phone_book.get('Jerzy'))
print(phone_book['Jerzy'])

print(phone_book.get('Jezy'))
# print(phone_book['Jery'])

phone_book['Ryszard'] = 78787877
print(phone_book)

del phone_book['Kamil']
print(phone_book)

deleted_phone_number = phone_book.pop('Jery', 'Ten nr nie zostal znaleziony')
print(deleted_phone_number)

# for element in phone_book: #wyswietla imiona
#     print(element)

# for element in phone_book.values(): #wyswietla wartosci
#     print(element)

# for element in phone_book.items():
#     print(element[0] +":" + str(element[1]))
# albo:

for name, phone_number in phone_book.items():
    print(name +":" + str(phone_book))

for item in phone_book.items():
    print(item)