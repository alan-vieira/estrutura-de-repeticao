# 37. Uma academia deseja fazer um senso entre seus
# clientes para descobrir o mais alto, o mais baixo,
# a mais gordo e o mais magro, para isto você deve fazer
# um programa que pergunte a cada um dos clientes da
# academia seu código, sua altura e seu peso. O final
# da digitação de dados deve ser dada quando o usuário
# digitar 0 (zero) no campo código. Ao encerrar o
# programa também deve ser informados os códigos e
# valores do clente mais alto, do mais baixo, do mais
# gordo e do mais magro, além da média das alturas e
# dos pesos dos clientes
#
# não está pronto


soma = 1
cont = -1
codigo = 1
altura = 1
peso = 1

altura_soma = 0
peso_soma = 0

print()
while(codigo != 0):
    codigo = int(input("Informe o código: "))
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))
    print()

    cont += 1
    altura_soma += altura
    peso_soma += peso

altura_media = altura_soma / cont
peso_media = peso_soma / cont

print("Media de altura {}".format(altura_media))
print("Media de peso {}".format(peso_media))