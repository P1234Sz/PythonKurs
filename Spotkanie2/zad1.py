def A (m, n):
    if m == 0:
        wynik = n + 1
    elif m > 0 and n == 0:
        wynik = A(m-1, 1)
    elif m > 0 and n > 0:
        wynik = A(m-1, A(m, n-1))

    return wynik


licz = A(0, 0)
print("Wynik dla A(0, 0)" + str(licz))

licz = A(1, 0)
print("Wynik dla A(1, 0)" + str(licz))

licz = A(1, 1)
print("Wynik dla A(1, 1)" + str(licz))

licz = A(3, 3)
print("Wynik dla A(3, 3)" + str(licz))
