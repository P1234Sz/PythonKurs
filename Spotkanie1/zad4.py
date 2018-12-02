def podatek(kwota):
    wynik = 0
    if kwota <= 44490:
        wynik = 44490 * (19/100)
    if 44490 < kwota <= 85528:
        wynik = 44490 * (19/100) + ((kwota - 44490)*(30/100))
    if kwota > 85528:
        wynik = (44490 * (19 / 100)) + (41038 * (30 / 100)) + ((kwota - 85528)*(40/100))
    return wynik


print(podatek(100000))