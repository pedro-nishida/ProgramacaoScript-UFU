#Pedro Henrique Fujinami Nishida
#12121ECP015
# # # # # # # # # # # #
# Knapsack's Problem  #
# # # # # # # # # # # #

#PROGRAMA PRINCIPAL
def main():
    #@category: ENTRADA
    #@desc: pergunta quantidade de itens(para montar as listas), peso limite da mochila, e atribui peso-valor na listas
    items, capacity = int(input()), int(input())
    weight, value= [int(input()) for n in range(items)], [int(input()) for n in range(items)]
    VD = [value[n]/weight[n] for n in range(items)] #razao que determina prioridade de itens pela maior valor, menor peso

    #@category: ESQUELETO DO PROGRAMA
    actual_Weight, actual_Value = 0, 0 #Variáveis armazena a somatoria dos valores e pesos contidos na mochila
    a = True  #indicador de passagem, condicao: termina quando as lista de itens esvaziar
    while a:

        notFIT(weight, actual_Weight, actual_Value, capacity, value, VD)
        n = priority(VD)

        if weight == []: #condicional para sair do loop de "while" e terminar o programa
            a = False
        #adiciona o item de prioridade se dentro da capacidade da mochila:
        elif (weight[n] + actual_Weight) <= capacity:
            actual_Value += value[n]
            actual_Weight += weight[n]
            del(weight[n], value[n], VD[n]) #deleta da lista o item previamente utilizado

    #@category: SAIDA E FIM DO PROGRAMA
    print("{}\n{}".format(actual_Value, actual_Weight))
    exit

########################################################################################################################
#@category: FUNÇÕES CRIADAS E FEITAS

#@desc: Função elimina itens que ultrapassara o limite da mochila caso adicionado
def notFIT(weight, actual_Weight, actual_Value, capacity, value, VD):
    for i in range(len(weight)):
        if (weight[i] + actual_Weight) > capacity:
            del(weight[i], value[i], VD[i])
            return weight, value, VD

#@desc: Função prioriza o item com maior valor e menor peso, atraves da comparacao de outros valores/pesos
def priority(lista):
    max, location = 0, 0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
            location = i
    return location
        
main()