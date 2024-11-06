def hello(name, age, last_name=None):
    print('Czesc ' + name + '! Masz ' + str(age) +'lat')
    if last_name is not None:
      print('Masz na nazwisko: ' + last_name)
# hello('Anna', 35)
# hello('Malin', 34)
# hello('Konrad', 57)

hello(age=35, name='Grzegorz', last_name = 'Norman')


def strip_and_uppercase(text):
    return str(text).strip().upper()

text = ' jestem tekstem dO zmiAny'
print(text)
text = strip_and_uppercase(text)
print(text)

