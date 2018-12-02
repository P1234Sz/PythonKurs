def suma_dzielnikow(n):
    suma = 0
    lista = []
    i = 1
    while i <= (n-1):
        if n % i == 0:
            suma = suma + 1
            lista.append(i)
        i = i + 1
    print("Liczba dzielnikow liczby ", n, "wynosi: ", suma)
    print(lista)
