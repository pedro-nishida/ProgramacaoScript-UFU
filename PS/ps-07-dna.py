#Pedro Henrique Fujinami Nishida
#12121ECP015

#PROGRAMA PRINCIPAL
def main():

    #@category: ENTRADA
    #@desc: transforma strings em listas com respectivas entradas, 
    dna, primer = list(input()), list(input())

    #@desc: Função verifica compatibilidade do "primer" com alguma posição do "dna"
    search(dna, primer)

######################################################################################

#@desc: transforma o primer para corresponder com a ligação com dna
def change(primer):
    primer = primer[::-1]   #inverte a lista primer
    primer = primer[1:-1]   #elimina o indice de inicio e fim do primer, "5" e "3"
    new_primer = []         #cria lista vazia que armazenará o primer esperado

    """@desc: loop que analisa item por item de forma a procurar compatibilidade
    do primer, e armazena-os na lisa new_primer."""
    for i in range(len(primer)):
        if primer[i] == "A":
            new_primer.append("T")
        elif primer[i] == "T":
            new_primer.append("A")
        elif primer[i] == "G":
            new_primer.append("C")
        elif primer[i] == "C":
            new_primer.append("G")
    return new_primer

#@desc: procura o padrão entre as duas listas, linear search, e printa essa posição ou se não há ligacao
def search(dna, primer):
    Found = False           #variável indica se pelo menos um padrão foi encontrado
    primer = change(primer) #chama a função de reordenar o primer como desejado

    for i in range(0,len(dna)): #varredura pela lista principal "dna" 
        if dna[i:i+len(primer)] == primer: #em caso de padrão
            print("Ligacao na posicao {}".format(i)) #imprime posição como saída e
            Found = True                             #indica se existe pelo menos um padrão

    print("Nenhuma ligacao") if not Found else exit()#se não, imprime a não ocorrencia.
main()