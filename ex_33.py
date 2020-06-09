# 33. O Departamento Estadual de Meteorologia lhe
# contratou para desenvolver um programa que leia
# as um conjunto indeterminado de temperaturas, e
# informe ao final a menor e a maior temperaturas
# informadas, bem como a média das temperaturas.

n = int(input("Digite a quantidade de temperaturas informadas: "))
soma = 0
maior = None
menor = None

for i in (range(n)):
    x = float(input("Digite um número: "))
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

media = soma / n

print('A maior temperatura é {} ºC e o menor é {} ºC'.format(maior,menor))
print("A média das temperaturas é {} ºC".format(media))