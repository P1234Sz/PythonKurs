def bmi_wylicz(masa, wzrost):
    bmi_wartosc = round(masa / (wzrost * wzrost), 2)
    return bmi_wartosc


def bmi_komentarz(bmi_wartosc):
    print("BMI: " + str(bmi_wartosc))
    if bmi_wartosc < 18.5:
        print("Niedowaga")
    elif 18.5 <= bmi_wartosc < 25:
        print("Wartosc prawidlowa")
    elif bmi_wartosc >= 25:
        print("Nadwaga")
    return


masa = float(input("Podaj mase [kg]: "))
wzrost = float(input("Podaj wzrost [m]: "))
bmi = bmi_wylicz(masa, wzrost)
bmi_komentarz(bmi)



# Test
print("\nTest dla masy 70kg i 1.7m wzrostu:")

if bmi_wylicz(70, 1.7) != 24.22:
    bmi_komentarz(bmi_wylicz(70, 1.7))
    print("Zle policzono!")
else:
    bmi_komentarz(bmi_wylicz(70, 1.7))
    print("Wynik poprawny")