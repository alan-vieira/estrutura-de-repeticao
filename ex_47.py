# 47. Em uma competição de ginástica, cada atleta recebe
# votos de sete jurados. A melhor e a pior nota são
# eliminadas. A sua nota fica sendo a média dos votos
# restantes. Você deve fazer um programa que receba o
# nome do ginasta e as notas dos sete jurados alcançadas
# pelo atleta em sua apresentação e depois informe a
# sua média, conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular
# a média com as notas restantes). As notas não são
# informados ordenadas. Um exemplo de saída do programa
# deve ser conforme o exemplo abaixo:
#
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04


nota = []
atleta = input("Atleta: ")

for i in range(7):
    nota.append(float(input("Nota: ")))

nota.sort() #coloca a lista em ordem

nota_maior = max(nota)
nota_menor = min(nota)

nota.pop(0) #elimina o primeiro termo da lista
nota.pop(-1) #elimina o último termo da lista

media = sum(nota) / len(nota)

print()
print("Resultado final:")
print("Atleta: {}".format(atleta))
print("Melhor nota: {}".format(nota_maior))
print("Pior nota: {}".format(nota_menor))
print("Média: {}".format(round(media,2)))

