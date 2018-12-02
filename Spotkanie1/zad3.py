def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i = i +1
        wynik = wynik * i
    return wynik

def suma_silni(n):
    i = 1
    wynik = 0
    while i <= n:
        wynik = wynik + silnia(i)
        i = i + 1
    return wynik

for i in range(3, 6):
    print('{0}: {1:5}'.format(i, suma_silni(i)))

