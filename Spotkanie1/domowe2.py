Nominaly = [20, 10, 5, 2, 1]
Kwota = int(input("Podaj kwote: "))


def Ile_wyjac (Kwota, Nominaly):
    i = 0
    while Kwota > 0:
        if Kwota >= Nominaly[i]:
            Ilosc = int(Kwota / Nominaly[i])
            Kwota = Kwota - (Nominaly[i] * Ilosc)
            print("Wyjmij " + str(Ilosc) + " razy " + str(Nominaly[i]))
        i = i + 1

Ile_wyjac(Kwota, Nominaly)

#Test
print("\nTest dla kwoty 123: \n6 x 20 \n1 x 2 \n1 x 1")
print("wynik: ")
Ile_wyjac(123, Nominaly)