# 39. Faça um programa que leia dez conjuntos de dois
# valores, o primeiro representando o número do aluno
# e o segundo representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo. Mostre
# o número do aluno mais alto e o número do aluno
# mais baixo, junto com suas alturas.

numero_alunos = []
altura_alunos = []
maior = None
menor = None

for index in range(4):
    numero_alunos.append(int(input("Digite o número do aluno: ")))
    altura_alunos.append(int(input("Digite a altura do aluno: ")))
    print()

#maior número
    if (maior != None and maior > altura_alunos[index]):
        maior = maior
    else:
        maior = altura_alunos[index]
        aluno_alto = index
# menor número
    if (menor != None and menor < altura_alunos[index]):
        menor = menor
    else:
        menor = altura_alunos[index]
        aluno_baixo = index

print('O maior aluno é {} e o menor é {}'.format(numero_alunos[aluno_alto],numero_alunos[aluno_baixo]))