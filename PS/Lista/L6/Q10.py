def main():
    
    lenght = int(input("digite a largura: "))
    height = int(input("digite a altura: "))

    nL = 0
    nH = 0

    while nH < height:

        if (nH == 0) or (nH == (height-1)):
            while nL < lenght:
                print("# ",end="")
                nL += 1

        else:
            while nL < lenght:
                if (nL == 0) or (nL == (lenght-1)):
                    print("# ",end="")
                else:
                    print("  ",end="")
                nL += 1

        nH += 1
        nL = 0
        print("")

main()