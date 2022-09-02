#Pedro Henrique Fujinami Nishida
#12121ECP015

#função armazena a matriz como lista(mapa)
def batalha():
    batalha,a = [],[] #lista vazia que armazenarÃ¡ os valores
    for i in range(10):  #loop de criar linhas, de acordo com a entrada
        a = input().split(" ") #separador de valores para as colunas
        batalha.append(a)  #esses valores sÃ£o adicionados como uma lista para a matriz
    return batalha


#funcao usa input para determinar posição do tiro
def atirar():
    linha, coluna = input().split(" ")
    linha, coluna = ord(linha)- 65, int(coluna) - 1
    return [linha,coluna]

#função principal
def main():
    mapa, frota = batalha(), []
    atingiu = False
    afundou = False
    for jogadas in range(int(input())):
        x,y = atirar()
        
        if not mapa[x][y] != ".":
            print("agua")
        else:
            if (mapa[x][y]).isupper():
                mapa[x][y]= (mapa[x][y]).lower()
            navio = mapa[x][y].upper()
                
            for i in range(10):
                for j in range(10):
                    if not navio in mapa[i][j]:
                        afundou = True
                if not afundou:
                    print("atingiu o navio {}".format(navio))
                else:
                    print("afundou o navio {}".format(navio))
                
        

if __name__ == '__main__':
    main()
