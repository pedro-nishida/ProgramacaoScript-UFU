lenght = int(input("digite a largura: "))
height = int(input("digite a altura: "))

nL = 0
nH = 0

while nH < height:

    while nL < lenght:
        print("#", end="")
        nL += 1

    nH += 1
    nL = 0
    print("")
