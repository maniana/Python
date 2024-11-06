countries = {
    'Polska': 'Warszawa',
    'Norwegia': 'Oslo',
    'Niemcy': 'Berlin',
    'Francja': 'Paryz',
    'Ukraina': 'Kijow'
}
for country, capital in countries.items():
    print(country + "-" + capital)

for country in sorted(countries):
    print(country + '-' + countries[country])