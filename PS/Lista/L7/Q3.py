temp = [20, 30 , 28, 17, 23, 10, 11, 8, 39, 30]

#alternativa a - 
print("A temperatura no 1o dia foi {}".format(temp[0]))

#alternativa b -
print("A temperatura no ultimo dia foi {}".format(temp[-1]))

#alternativa c -
#print("A temperatura maxima = {}".formtat(max(temp)))

maximo = temp[0]
for i in range (len(temp)):
    if(temp[i] > maximo):
        maximo = temp[i]

print("A máxima temperatura foi {}".format(maximo))

#alternativa d
print("o dia mais quente foi {}".format(temp.index(max(temp))))

#alternativa e)
print(min(temp))

#alternativa f)
print(temp.index(min(temp)))

#alternativa g)

soma = 0
i= 0

while i < len(temp):
    soma += temp[1]
    i += 1
media = soma/len(temp)
print("media de temperatura é {}".format(media))

from statistics import mean
print("media de temperatura é {}".format(mean(temp)))