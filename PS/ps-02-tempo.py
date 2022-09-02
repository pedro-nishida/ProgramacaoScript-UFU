#Pedro Henrique Fujinami Nishida
#12121ECP015

# Trabalho 2 - Convesão de tempo.
#Entrada:
tempo = int(input())

#Conversão
def convert(tempo):

    #Convesão de dias:
    dias = tempo // (24 * 3600) #Divisão de segundos para dias
    resto = tempo % (24 * 3600) #Resto da divisão e armazena em nova váriavel

    #Conversão de horas:
    horas = resto // 3600 #Divisão do resto de cima para saber horas
    resto %= 3600 #Novo valor para variável a partir da divisão de cima

    #Conversão de minutos:
    minutos = resto // 60 #Divisão a partir da variável resto para saber minutos
    
    #Determina os segundos restantes da conversão:
    segundos = resto % 60 #elimina segundos já convertidos para minutos

    #Retorno da função convert():
    return("{} dia(s), {} hora(s), {} minuto(s) e {} segundo(s).".format(dias, horas, minutos, segundos))

#Saída:
print(convert(tempo))
