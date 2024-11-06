countries_information ={}
countries_information['Polska'] = ('Warszawa', 38)
countries_information['Niemcy'] = ('Berlin', 83)
countries_information['Francja'] = ('Paryz', 57)


def print_country_information(country):
    print('Kraj: ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkancow: ' + str(countries_information[country][1]) + ' milionow')

print_country_information('Polska')
print()

print_country_information('Niemcy')
print()