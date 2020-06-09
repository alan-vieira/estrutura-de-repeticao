# 6. Faça um programa que imprima na tela os números
# de 1 a 20, um abaixo do outro. Depois modifique
# o programa para que ele mostre os números um ao
# lado do outro.

"""i = 1
while(i <= 10):
    print(i)
    i += 1"""

# impressão dos números na horizontal
i = 1
while(i <= 10):
    print(i,end =" ")
    i += 1

for i in (range(1,21,1)):
    print(i,end=" ")
