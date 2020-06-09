# 25. Faça um programa que peça para n pessoas a sua
# idade, ao final o programa devera verificar se a
# média de idade da turma varia entre 0 e 25,26 e 60
# e maior que 60; e então, dizer se a turma é jovem,
# adulta ou idosa, conforme a média calculada.

n = int(input("Digite N: "))
soma = 0

for i in (range(n)):
    x = int(input("Digite a sua idade: "))
    soma += x

media = soma / n

if(media >= 0 and media <= 25):
    print("A turma é jovem")

if(media >= 26 and media <= 60):
    print("A turma é adulta")

if(media >= 61):
    print("A turma é idosa")