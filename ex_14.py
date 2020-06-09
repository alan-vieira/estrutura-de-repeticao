# 14. Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

numero = 1
par = 0
impar = 0
while(numero <= 10):
    if ((numero % 2 == 0)):
        print("Par:",numero)
        par += 1
    else:
        print("Ímpar:",numero)
        impar += 1
    numero += 1
print("Números pares: ",par)
print("Números ímpares: ",impar)