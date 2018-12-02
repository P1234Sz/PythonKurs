def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat

def vat_paragon(lista):
    suma = 0
    for element in lista:
        suma = suma + 0.23*element
    vat = round(suma, 2)
    return vat


zakupy = [0.2, 0.5, 4.59, 6, 3.33]
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))