#Pedro Henrique Fujinami Nishida
#12121ECP015

############################
#ALGORITIMO DE SIMILARIDADE#
############################

#@type: FUNCOES USADAS

#@desc: cria matriz(lista dentro de lista) com formato quadrado de n linhas
#       e n colunas de acordo com primeira entrada
def matrix():
    matriz = [] #lista vazia que armazenará os valores
    for i in range(int(input())):  #loop de criar linhas, de acordo com a entrada
        a = [int(x) for x in input().split(" ")] #separador de valores para as colunas
        matriz.append(a)  #esses valores são adicionados como uma lista para a matriz
    return matriz        
    
#@desc: funcao principal que analisa todas as possibilidades da matriz menor estar contida na maior
def verify(big, small):
    #criando variáveis:
    linha, coluna, similar  = 0, 0, 0.00
    iguais = 0

    #@desc usa loops para cada posicao(linha, coluna) da matrizes, respectivamente a maior e a menor.
    for linha_maior in range(len(big)-len(small)+1):
        for coluna_maior in range(len(big)-len(small)+1):

            for linha_menor in range(len(small)):
                for coluna_menor in range(len(small)):
                    
                    #@desc: acumulativa de igualdade na condição dos itens serem iguais
                    if small[linha_menor][coluna_menor] == big[linha_maior + linha_menor][coluna_maior + coluna_menor]:
                        iguais += 1

            porcentagem = (iguais/(len(small)**2))*100.00 #razão termos iguais pelo total da matriz menor
            iguais = 0 #reseta variável acumulativa para proxima comparação

            #@desc: na condição da atual posição ser maior que as demais, aramzena sua porcentagem e sua posição
            if porcentagem > similar:
                similar = porcentagem
                linha, coluna = linha_maior, coluna_maior
    
    #@type: SAIDA
    print("Posição: ({},{})\nSimilaridade máxima: {}%".format(linha, coluna, ("%.2f" % similar)))

###############################################################################

#@type: FUNCAO MAIN
def main():
    #guarda matriz na variável, a partir da convocação da função criadora de matrizes
    matriz_maior = matrix()
    matriz_menor = matrix()
    
    #chama a funcao de comparacao de matrizes
    verify(matriz_maior, matriz_menor)
     
#chama a funcao principal
main()