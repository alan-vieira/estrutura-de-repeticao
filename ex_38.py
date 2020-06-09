# 38. Um funcionário de uma empresa recebe aumento salarial
# anualmente: Sabe-se que:
#
# Esse funcionário foi contratado em 1995, com salário
# inicial de R$ 1.000,00;
#
# Em 1996 recebeu aumento de 1,5% sobre seu salário
# inicial;
#
# A partir de 1997 (inclusive), os aumentos salariais
# sempre correspondem ao dobro do percentual do ano
# anterior. Faça um programa que determine o salário
# atual desse funcionário. Após concluir isto, altere
# o programa permitindo que o usuário digite o salário
# inicial do funcionário.

"""salario = 1000.00
porcentagem = 0.0
ano = 1995
print("{} - {}% - R$ {}".format(ano,porcentagem,salario))
porcentagem = 1.5

for i in range((ano +1),(1998 + 1)):
    salario = (salario + ((salario * porcentagem) / 100))
    print("{} - {}% - R$ {}".format(i,porcentagem,salario))
    porcentagem *= 2"""

salario = float(input("Infome o salário: R$ "))
porcentagem = 0.0
ano = 1995
print("{} - {}% - R$ {}".format(ano,porcentagem,salario))
porcentagem = 1.5

for i in range((ano +1),(1997 + 1)):
    salario = (salario + ((salario * porcentagem) / 100))
    print("{} - {}% - R$ {}".format(i,porcentagem,salario))
    porcentagem *= 2