def suma_dzielnikow(n):
    suma = 0
    lista = []
    i = 1
    while i <= (n-1):
        if n % i == 0:
            lista.append(i)
        i = i + 1
    for element in lista:
        suma = suma + element
    print("Dzielniki liczby ", n, ":")
    print(lista)
    print("Ich suma to: ", suma)
    return

suma_dzielnikow(6)