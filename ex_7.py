# 7. Faça um programa que leia 5 números e informe o
# maior número.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))

maior = numero1
if (numero2 > maior):
    maior = numero2

if (numero3 > maior):
    maior = numero3

if (numero4 > maior):
    maior = numero4

if (numero5 > maior):
    maior = numero5

print("Maior: ",maior)