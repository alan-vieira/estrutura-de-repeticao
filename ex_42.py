# 42. Faça um programa que leia uma quantidade indeterminada
# de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75]
# e [76-100]. A entrada de dados deverá terminar quando
# for lido um número negativo.


grupo1 = 0
grupo2 = 0
grupo3 = 0
grupo4 = 0
numero = 101

print()
while(numero > 0):
    numero = float(input("Digite um número: "))

    if(numero >= 0 and numero <= 25):
        grupo1 += 1
    if (numero >= 26 and numero <= 50):
        grupo2 += 1
    if (numero >= 51 and numero <= 75):
        grupo3 += 1
    if (numero >= 76 and numero <= 100):
        grupo4 += 1

print("O intervaldo de [0-25] possui {} número(s)".format(grupo1))
print("O intervaldo de [26-50] possui {} número(s)".format(grupo2))
print("O intervaldo de [51-75] possui {} número(s)".format(grupo3))
print("O intervaldo de [76-100] possui {} número(s)".format(grupo4))
