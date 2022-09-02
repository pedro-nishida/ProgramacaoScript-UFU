#conversor de segundos para HH:MM:SS

#Entrada
segundos = int(input())

#Conversão
def convert(segundos):
    segundos %= 24 * 3600 #elimina os segundos equivalentes a mais de um dia

    #calcula e armazena em respectivas variáveis
    horas = segundos // 3600 
    segundos %= 3600 #elimina segundos já convertidos para horas
    minutos = segundos // 60
    segundos %= 60 #elimina segundos já convertidos para minutos

    return("{}:{}:{}".format(horas, minutos, segundos))

print(convert(segundos))
