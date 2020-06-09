# 27. Faça um programa que calcule o número médio de
# alunos por turma. Para isto, peça a quantidade de
# turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

count = 0
soma = 0

turmas = int(input("Informe o número de turmas: "))
while (turmas != count):
    alunos = int(input("Digite o número de alunos: "))

    while (alunos > 40):
        alunos = int(input("Digite o número de alunos:[erro]: "))

    count += 1
    soma += alunos

media = soma / turmas

print("A média de alunos por turma é: ",round(media))