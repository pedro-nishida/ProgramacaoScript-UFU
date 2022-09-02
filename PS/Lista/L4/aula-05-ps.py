entrada = int(input())
soma=0

while (entrada != 0):
    soma = soma + (entrada % 10)
    entrada //= 10


print(soma)