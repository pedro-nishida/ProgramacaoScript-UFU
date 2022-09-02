a = 5
def fun1():
    a = 1
    print(a) #Output1, printa variável local
def fun2(a):
    a += 3
    print(a) #Output2, imprime operação a partir da variável global
def fun3():
    ## Chama variável global para interior da função
    global a
    ##------------------------##
    print(a)


fun1()#chama função 1 e roda o primeiro Output
fun2(a)
print(a) #imprime a variável global
b=7
fun3()
b=9
fun2() #ERRO: falta de parâmetro para função
print(b)