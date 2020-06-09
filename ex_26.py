# 26. Numa eleição existem três candidatos. Faça um
# programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar
# o número de votos de cada candidato.


eleitor_total = int(input("Informe o número total de eleitores: "))
um = 0
dois = 0
tres = 0

for i in (range(eleitor_total)):
    eleitor = int(input("Eleitor digite o número do seu candidato: "))

    if(eleitor == 1):
        um += 1

    if (eleitor == 2):
        dois += 1

    if (eleitor == 3):
        tres += 1

print("O candidato 1 recebeu",um,"voto(s)")
print("O candidato 2 recebeu",dois,"voto(s)")
print("O candidato 3 recebeu",tres,"voto(s)")