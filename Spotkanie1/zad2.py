def piramida(n):
    rozmiar = (2*n) - 2
    for i in range (n+1):
        for j in range(rozmiar):
            print (end=" ")
        rozmiar = rozmiar - 1
        for j in range(i+1):
            print("#", end=' ')
        print(" ")
    return


piramida(4)