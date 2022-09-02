#Pedro Henrique Fujinami Nishida
#12121ECP015

#PROGRAMA DE DISTRIBUIÇÃO DE VACINAS

def main():
    #VARIÁVEIS

    d1  = 0               #Pessoas totalmente imunizadas
    d2  = 0               #Pessoas imunizadas apenas com uma dose
    d   = 0               #Pessoas tomou uma dose há um mês
    d2a = 0               #Pessoas que tomaram seguda dose com atraso
    d1a = 0               #Pessoas esperando a segunda dose com atraso

    N = int(input())

    while (N != 0):
        vaxx = int(input())

        if d1a == 0:

            if d1 == 0:
                d1 = vaxx

            elif d1 != 0 and d1 <= vaxx:
                vaxx -= d1
                d2 += d1
                d1 = vaxx
            
            elif d1 != 0 and d1 > vaxx:
                d2 = vaxx
        
        elif (d1a != 0) and (d1a <= vaxx):

            vaxx -= d1a
            d2a = d1a
            d1a = 0
                
            if d1 == 0:
               d1 = vaxx

            elif d1 != 0 and d1 <= vaxx:
                vaxx -= d1
                d2 += d1
                d1 = vaxx
            
            elif d1 != 0 and d1 > vaxx:
                d2 += vaxx 
        
        elif (d1a != 0) and (d1a >= vaxx):
                d2a = vaxx
                d1a -= vaxx

        if d != 0:
            if vaxx > d:
                d2 = d
                d = 0
            else:
                d1a = d - vaxx
                d2 = vaxx

        N -= 1
        
    saida(d2, d1, d2a, d1a)

def saida(a, b, c, d):                                      #Formato da saída conforme pedido
    print("Pessoas completamente imunizadas: {}".format(a+c))
    print("Pessoas imunizadas apenas com uma dose: {}".format(b+d))
    print("Pessoas que tomaram a segunda dose com atraso: {}".format(c))
    print("Pessoas esperando a segunda dose com atraso: {}".format(d))

main()