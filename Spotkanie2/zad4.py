def pierwsza(n):
    lista = []
    i = 1
    while i <= (n - 1):
        if n % i == 0:
            lista.append(i)
        i = i + 1
    if len(lista) == 1:
        print(n, "jest liczba pierwsza")
    else:
        print(n, "nie jest liczba pierwsza")


