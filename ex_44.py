# 44. Em uma eleição presidencial existem quatro
# candidatos. Os votos são informados por meio de
# código. Os códigos utilizados são:
#
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de
# votos. Para finalizar o conjunto de votos tem-se
# o valor zero.


voto = -1
um = 0
dois = 0
tres = 0
quatro = 0
nulo = 0
branco = 0

while(voto != 0):
    print()
    print("Vote: 1- Jose/ 2- João/ 3- Maria/ 4- Tânia")
    voto = int(input("Digite seu voto: "))

    if(voto == 1):
        um += 1

    if (voto == 2):
        dois += 1

    if (voto == 3):
        tres += 1

    if (voto == 4):
        quatro += 1

    if (voto == 5):
        nulo += 1

    if (voto == 6):
        branco += 1
print()
voto_total = um + dois + tres + quatro + nulo + branco
nulo_percente = ((100 * nulo) / voto_total)
branco_percete = ((100 * branco) / voto_total)

print("Jose recebeu",um,"voto(s)")
print("João recebeu",dois,"voto(s)")
print("Maria recebeu",tres,"voto(s)")
print("Tânia recebeu",quatro,"voto(s)")
print("Nulo recebeu {} voto(s) {}% do total".format(nulo,(round(nulo_percente,2))))
print("Branco recebeu {} voto(s) {}% do total".format(branco,(round(branco_percete,2))))
