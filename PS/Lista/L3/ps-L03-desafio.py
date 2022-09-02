#Algorítimo para classificação etária

#Entrada
idade = int(input("Digite sua idade: "))

#Criando uma função para o algorítimo
def classe(idade):
    if (idade <= 12):
        return("criança")
    elif (idade <= 18):
        return("adolecente")
    elif (idade <= 60):
        return("adulto")
    else:
        return("idoso")

#Saída
print("Você está na fase", classe(idade))