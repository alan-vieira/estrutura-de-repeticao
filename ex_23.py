# 23. Faça um programa que mostre todos os primos entre
# 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões
# que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número
# de testes (divisões) executados.

n = int(input("Digite valor final do conjunto de números: "))
divisoes = 1

for numero in range(1,(n+1)):
    mult = 0
    count = 0


    if numero % 2 == 1 and numero != 2:
        divisoes += 1
    else:
        divisoes += 1

    for count in range(2,numero):
        if (numero % count == 0):
            mult += 1

    if (mult == 0):
        print (numero,end=" ")
print()
print("Número de divisões", divisoes)
