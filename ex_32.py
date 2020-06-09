# 32. Faça um programa que calcule o fatorial de um
# número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme
# o exemplo abaixo:
#
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

n = int(input("Informe o n fatorial: "))
fatorial = 1
print("{}! =".format(n), end=" ")
for i in reversed (range(2,(n + 1))):
    fatorial *= i
    print(i,end=" . ")
print("1 =",fatorial)