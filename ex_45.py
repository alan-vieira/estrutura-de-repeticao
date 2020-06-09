# 45. Desenvolver um programa para verificar a nota do
# aluno em uma prova com 10 questões, o programa deve
# perguntar ao aluno a resposta de cada questão e ao
# final comparar com o gabarito da prova e assim calcular
# o total de acertos e a nota (atribuir 1 ponto por
# resposta certa). Após cada aluno utilizar o sistema
# deve ser feita uma pergunta se outro aluno vai utilizar
# o sistema. Após todos os alunos terem respondido
# informar:
#
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
#
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
#
# Após concluir isto você poderia incrementar o
# programa permitindo que o professor digite o
# gabarito da prova antes dos alunos usarem o programa.

"""
gabarito = ["a","b","c","d","e","e","d","c","b","a"]
resposta = ['','','','','','','','','','']
aluno = []
aluno_resposta = 0
cont = 1

while(True):
    print("Aluno {}".format(cont))

    #questões
    for item in range (len(gabarito)):
        resposta[item] = input("Questão {}: ".format(item+1))

        if (resposta[item] == gabarito[item]):
            aluno_resposta += 1

    aluno.append(aluno_resposta)

    aluno_resposta = 0
    cont += 1
    print()

    reset = input("Outro aluno utilizara o sistema? Pressione 0 para continuar, 1 para encerrar: ")
    if reset == "0":
        print()
        continue
    else:
        print()
        print("Encerrando...")
        print()
        break

media = sum(aluno) / len(aluno)

print("Maior acerto: {}".format(max(aluno)))
print("Mentor acerto: {}".format(min(aluno)))
print("Total de alunos: {}".format(len(aluno)))
print("Média das notas: {}".format(media))

"""


gabarito = []
resposta = ['', '', '', '', '', '', '', '', '', '']
aluno = []
aluno_resposta = 0
cont = 1

#gabarito
for i in range(10):
    gabarito.append(input("Digite o gabarito da questão {}: ".format(i+1)))
    continue
print()
print()

#aluno prova
while (True):
    print("Aluno {}".format(cont))

    # questões
    for item in range(len(gabarito)):
        resposta[item] = input("Questão {}: ".format(item + 1))

        if (resposta[item] == gabarito[item]):
            aluno_resposta += 1

    aluno.append(aluno_resposta)

    aluno_resposta = 0
    cont += 1
    print()

    reset = input("Outro aluno utilizara o sistema? Pressione 0 para continuar, 1 para encerrar: ")
    if reset == "0":
        print()
        continue
    else:
        print()
        print("Encerrando...")
        print()
        break

media = sum(aluno) / len(aluno)

print("Maior acerto: {}".format(max(aluno)))
print("Mentor acerto: {}".format(min(aluno)))
print("Total de alunos: {}".format(len(aluno)))
print("Média das notas: {}".format(media))
