def Odsetki (oproc, czas, kwota):
    odsetki = kwota * oproc * czas / 12
    return odsetki


licz = Odsetki (0.03, 3, 1000)
print(licz)

i = 0
kwota = 1000
while i < 4:
    kwota = kwota + Odsetki(0.03, 3, kwota)
    i = i + 1

print("Odnawialna = " + str(round(kwota, 2)))
print("Caloroczna = " + str(1000 + Odsetki(0.03, 12, 1000)))