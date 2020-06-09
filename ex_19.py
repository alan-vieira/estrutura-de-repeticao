# 19. Altere o programa anterior para que ele aceite
# apenas números entre 0 e 1000.

count = 0
soma = 0
maior = None
menor = None

quant = int(input("Digite a quantidade de números do conjunto: "))
while (quant != count):
    numero = int(input("Digite um número: "))

    while (numero > 1000 or numero < 0):
        numero = int(input("Digite um número[erro]: "))

    count += 1

    soma += numero
    # maior número
    if (maior != None and maior > numero):
        maior = maior
    else:
        maior = numero

    # menor número
    if (menor != None and menor < numero):
        menor = menor
    else:
        menor = numero

print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
print("Soma: ", soma)