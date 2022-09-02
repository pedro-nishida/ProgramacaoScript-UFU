#Pedro Henrique Fujinami Nishida
#12121ECP015
########################################
#Castelo Ra-Tim-Bum: Senha do Porteiro.#
########################################

def main():
    
    #@category: entrada
    #@desc: divide e armazena cada inteiro como um item da lista    
                                                    #@example: 4 5 6 7 1 2 3
    lista = [int(i) for i in input().split(" ")]    #@return [4, 5, 6, 7, 1, 2, 3]

    
    for loop_limit in range(len(lista)):           #loop rotacina e verifica ate o limite, o numero de itens na lista
        rotaciona(lista)
        
        if verifica(lista):                        #verifica se a lista esta em ordem crescente, e o Porteiro "libera" passagem
            print("Klift, Kloft, Still, a porta se abriu")
            quit()

    #se mesmo apos varias rotacoes nenhum padrao afirma senha correta, o Porteiro "bloqueia" passagem
    print("Senha incorreta")


#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-#


#@desc: funcao troca os itens da lista de dois em dois, de direita para esquerda, finalizando em uma rotação completa dos itens
#@param {list[}}
def rotaciona(lista):                       #@example:                          
    for i in range(len(lista) - 1):         # i = 0, lista[4, 5, 6, 7, 1, 2, 3]  | i = 1, lista[5, 4, 6, 7, 1, 2, 3]
        acc = lista[(i+1)]                  # acc = 5                            | acc = 6
        lista[(i+1)] = lista[i]             # [4, 4, 6, 7, 1, 2, 3]              | [5, 4, 4, 7, 1, 2, 3]
        lista[i] = acc                      # [5, 4, 6, 7, 1, 2, 3]              | [5, 6, 4, 7, 1, 2, 3]

    return list                             # list[5, 6, 7, 1, 2, 3, 4]

#@desc: funcao que verifica a sequencia dos itens se e crescente (retorna 1, "True") ou nao (retorna 0, "False")
#@param {list[]}
def verifica(lista):
    comparacao = 1                          
    for i in range(len(lista) - 1):         #considerando cada verificação de dois por dois uma proposição, sendo 1 como True, 0 como Falso,
        if lista[i] < lista[i+1]:           #a  multiplicacao em "comparacao *= x", serve como uma formula logica proposicional: 
            comparacao *= 1                 #        p^q^r^s^t      ; onde todos os itens devem estar em sequencia crescente, caso contrario,
        else:                               # qualquer proposição falsa resultará em toda lista como não crescente
            comparacao *= 0
    return comparacao

main()