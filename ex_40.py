# 40. Foi feita uma estatística em cinco cidades brasileiras
# para coletar dados sobre acidentes de trânsito. Foram
# obtidos os seguintes dados:
#
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999).
#
# Deseja-se saber:
#
# Qual o maior e menor índice de acidentes de transito
# e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades
# com menos de 2.000 veículos de passeio.

codigo_cidade = []
quandidade_veiculo = []
quandidade_acidentes = []
maior_indice = None
menor_indice = None

veiculos_soma = 0
acidentes_soma = 0
cont = 0

for index in range(5):
    codigo_cidade.append(int(input("Digite o código da cidade: ")))
    quandidade_veiculo.append(int(input("Digite o número de veículos: ")))
    quandidade_acidentes.append(int(input("Digite o número de aceidentes com vítima: ")))
    print()

#soma
    veiculos_soma += quandidade_veiculo[index]

    if (quandidade_acidentes[index] < 2000):
        acidentes_soma += quandidade_acidentes[index]
        cont += 1

#maior índice
    if (maior_indice != None and maior_indice > quandidade_acidentes[index]):
        maior_indice = maior_indice
    else:
        maior_indice = quandidade_acidentes[index]
        acidentes_alto = index
# menor número
    if (menor_indice != None and menor_indice < quandidade_acidentes[index]):
        menor_indice = menor_indice
    else:
        menor_indice = quandidade_acidentes[index]
        acidentes_baixo = index

print('A cidade {} tem o maior íncice de acidentes e a cidade {} tem o menor'.format(codigo_cidade[acidentes_alto],codigo_cidade[acidentes_baixo]))
print("A média de veículos de todas as cidades é {}".format(veiculos_soma / 5))
print("A média de acidentes de todas as cidades é {}".format(acidentes_soma / cont))