# 18. Faça um programa que, dado um conjunto de N números
# , determine o menor valor, o maior valor e a soma dos
# valores.

n = int(input("Digite N: "))
soma = 0
maior = None
menor = None

for i in (range(n)):
    x = int(input("Digite um número: "))
    soma += x
# maior número
    if (maior != None and maior > x):
        maior = maior
    else:
        maior = x

# menor número
    if (menor != None and menor < x):
        menor = menor
    else:
        menor = x

print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))
print("Soma: ",soma)