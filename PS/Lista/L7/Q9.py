def main():
    lista = []
    n = int(input("Digite o elemento da sua lista ="))

    for i in range(n):
        valor = int(input("Digite o elmento da sua lista ="))
        print("Sua lista e: {}".format(lista))
        C = int(input("Digite o C: !")) 

    i = 0
    while i<n:
        j = i + 1
        while j<n:
            if lista[i]*lista[j] == C:
                print("Elemento [{}] x Elemento [{}] = {}".format(i, j, C))
                encontrou = True

    if (not encontrou):
        print("Não Há")

main()
