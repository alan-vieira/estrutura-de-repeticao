# 24. Faça um programa que calcule o mostre a média
# aritmética de N notas.

n = int(input("Digite N: "))
soma = 0

for i in (range(n)):
    x = int(input("Digite um número: "))
    soma += x

media = soma / n

print("A média é: ",media)