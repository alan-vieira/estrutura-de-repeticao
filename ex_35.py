# 35. Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números
# primos existentes entre 1 e um número inteiro
# informado pelo usuário.

n = int(input("Digite valor final do conjunto de números: "))
divisoes = 1

for numero in range(1,(n+1)):
    mult = 0
    count = 0


    for count in range(2,numero):
        if (numero % count == 0):
            mult += 1

    if (mult == 0):
        print (numero,end=" ")
print()