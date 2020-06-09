# 8. Faça um programa que leia 5 números e informe a
# soma e a média dos números.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))

soma = (numero1 + numero2 + numero3 + numero4 + numero5)
media = soma / 5

print("A soma é igual a: ",soma)
print("A média é igual a: ",media)