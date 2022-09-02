def main():
    a = []

    valor = 1

    while (valor != 0):
        valor = int(input("Digite um numero: "))
        a.append(valor)
    
    i = len(a)
    for i in range (n - 1, -1, -1):

        print("Lista [{}] = {}".format(i,a[i]))
main()