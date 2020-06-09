# 28. Faça um programa que calcule o valor total investido
# por um colecionador em sua coleção de CDs e o valor
# médio gasto em cada um deles. O usuário deverá informar
# a quantidade de CDs e o valor para em cada um.

count = 0
soma = 0

cd_total = int(input("Informe a quantidade total de CDs: "))
while (cd_total != count):
    cd_valor = float(input("Digite o valor do CD: "))
    count += 1
    soma += cd_valor

media = soma / cd_total

print("O valor total investido é de R$",soma)
print("O valor medio de cada CD é de R$",media)