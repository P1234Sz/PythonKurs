def pierwsza(n, lista_dzielnikow_pierwszych):
    lista = []
    i = 1
    while i <= (n - 1):
        if n % i == 0:
            lista.append(i)
        i = i + 1
    if len(lista) == 1:
        print(n, "jest liczba pierwsza")
        lista_dzielnikow_pierwszych.append(n)
    else:
        print(n, "nie jest liczba pierwsza")
    return


def dzielniki_pierwsze(n):
    lista_dzielnikow_pierwszych = []
    lista_dzielnikow = []
    i = 1
    while i <= n:
        if n % i == 0:
            lista_dzielnikow.append(i)
        i = i + 1
    print("Lista wszystkich dzielnikow: ", lista_dzielnikow)
    for element in lista_dzielnikow:
        pierwsza(element, lista_dzielnikow_pierwszych)
    print("Lista dzielnikow pierwszych: ", lista_dzielnikow_pierwszych)
    return


def doskonala(n, lista_doskonalych):
    lista = []
    i = 1
    while i <= (n - 1):
        if n % i == 0:
            lista.append(i)
        i = i + 1
    if n == sum(lista):
        print(n, "jest liczba doskonala")
        lista_doskonalych.append(n)
    return

#pierwsza(2)
#pierwsza(3)
#pierwsza(5)

#dzielniki_pierwsze(121)


def cztery_doskonale():
    lista_doskonalych = []
    i = 1
    while len(lista_doskonalych) < 4:
        doskonala(i, lista_doskonalych)
        i = i + 1
    print(lista_doskonalych)
    return


cztery_doskonale()