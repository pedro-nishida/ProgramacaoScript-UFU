#Pedro Henrique Fujinami Nishida
#12121ECP015
#------------------------------------------
#       Jogo Avatar: Domínio de Aang 
#------------------------------------------

#Definição de variáveis
fire=0
water=0
earth=0
air=0
run = True                    #Indicador de passagem: continua ou interrompe jogo

while (run == True):                            #Roda a entrada e os calculos em loop até que o jogador indique para parar
    #Entrada para o Jogo:
    command_type = input()                      #Especifíca o elemento treinado(W,F,A,E) ou interrompe o jogo (X)

    #Selecionado Fire                           
    if (command_type == "F"):                   #Se enviado "F" para treinar FOGO:
        command_intesity = float(input())                  #~ Pede a pontuação para o treino
        fire += command_intesity              #~ ADICIONA pontuação ao elemento fogo
        water -= command_intesity/2          #~ Diminui o elemento agua pela metade da pontuação selecionado

    #Selecionado Water
    elif (command_type == "W"):                 #Se enviado "W" para treinar ÁGUA:
        command_intesity = float(input())                   #~ Pede a pontuação para o treino
        water += command_intesity            #~ ADICIONA pontuação ao elemento ÁGUA
        fire -= command_intesity/2              #~ DIMINUI o elemento FOGO pela metade da pontuação selecionado
    
    #Selecionado Earth
    elif (command_type == "E"):                 #Se enviado "W" para treinar TERRA:
        command_intesity = float(input())                  #~ Pede a pontuação para o treino
        earth += command_intesity            #~ ADICIONA pontuação ao elemento TERRA
        air -= command_intesity/2              #~ DIMINUI o elemento AR pela metade da pontuação selecionado

    #Selecionado Water
    elif (command_type == "A"):                 #Se enviado "W" para treinar AR:
        command_intesity = float(input())                   #~ Pede a pontuação para o treino
        earth -= command_intesity/2         #~ ADICIONA pontuação ao elemento AR
        air += command_intesity               #~ DIMINUI o elemento TERRA pela metade da pontuação selecionado

    elif (command_type == "X"):                 #Comando para parar o jogo
        run = False

    #Se valores de elementos forem igual ou menor a zero, seus valores serão 0.0:
    if fire <= 0:
        fire = 0.0
    if water <= 0:
        water = 0.0
    if earth <= 0:
        earth = 0.0
    if air <= 0:
        air = 0.0

#Saída
#Mostra a Pontuação do Jogador
print("Pontuacao Final\nAgua: {}\nTerra: {}\nFogo: {}\nAr: {}".format(water, earth, fire, air,))

#Mostra se o jogador venceu ou não, a partir de mensagem dirigida
if (fire*water*earth*air != 0):                     #entende-se:qualquer seja uma variável igual a zero, condição True
    print("Treinamento realizado com sucesso.")           # O jogador conseguiu treinar os 4 elementos(vence)
else:
    print("Realize mais treinamentos.")                   # O jogador perdeu afinidade com pelo menos um elemento(perde)       