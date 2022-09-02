def cria_matriz(linha, coluna):

    M = []
    for i in range(linha):
        linha = [int(i) for i in input("Digite a linha [{}]: ".format(i)).split()]
        M.append(linha)
    return M

def imprime(M, l, c):
    for linha in range(l):
        for coluna in range(c):
            print(M[linha][coluna], end = "  \t")
        print("")
            
def dimensoes(M):
    n_linhas  = len(M)
    n_coluna = 0
    
    if n_linhas > 0:
        n_colunas = len(M[0])

    dim = "{} x {}".format(n_linhas, n_colunas)


def main():

    linha = int(input())
    coluna = int(input())
    imprime(cria_matriz(linha, coluna), linha, coluna)

main()

#Questão 06, aulas 9.6
#Questão 08, aula 9.9
#Questão 09, aula 9.7
#Questão 10, aula 9.8
