# 41. Faça um programa que receba o valor de uma dívida
# e mostre uma tabela com os seguintes dados: valor da
# dívida, valor dos juros, quantidade de parcelas e
# valor da parcela.
#
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
#
# Quantidade de Parcelas  % de Juros sobre o valor
# inicial da dívida
#
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
#
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


valor_divida = float(input("Digite o valor da divida: "))

juros = [0,10,15,20,25]
parcela = [1,3,6,9,12]
print()
print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
for indice in range(len(juros)):
    valor_juros = ((valor_divida * juros[indice])/100)
    divida = (valor_divida + valor_juros)
    valor_parcela = divida/parcela[indice]
#   print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
    print("R$ {}        {}              {}                      R$ {}".format(divida,valor_juros,parcela[indice],valor_parcela))
