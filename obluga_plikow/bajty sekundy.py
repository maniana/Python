def download_time(file_size_mb, speed_bps):
    # Przeliczamy rozmiar pliku z megabajtów na bity
    file_size_bits = file_size_mb * 8 * 1_000_000  # 1 MB = 8 milionów bitów

    # Obliczamy czas pobierania w sekundach
    time_seconds = file_size_bits / speed_bps

    # Przeliczamy czas na minuty i godziny
    hours = int(time_seconds // 3600)
    minutes = int((time_seconds % 3600) // 60)
    seconds = int(time_seconds % 60)

    return hours, minutes, seconds


# Pobranie danych od użytkownika
file_size = float(input("Podaj rozmiar pliku w MB: "))
speed = float(input("Podaj prędkość internetu w bitach na sekundę (bps): "))

# Obliczenie czasu pobierania
hours, minutes, seconds = download_time(file_size, speed)

# Wyświetlenie wyniku
print(
    f"Czas pobierania pliku o rozmiarze {file_size} MB przy prędkości {speed} bps wynosi: {hours} godziny, {minutes} minuty, {seconds} sekundy.")
