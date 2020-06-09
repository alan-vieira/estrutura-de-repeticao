# 16. A série de Fibonacci é formada pela seqüência
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa
# que gere a série até que o valor seja maior que 500.

n = 1
termo = 1
ultimo = 0
penultimo = 1

while(termo <= 500):
    cont = 2
    while (cont <= (n + 1)):
        termo = ultimo + penultimo
        penultimo, ultimo = ultimo, termo
        cont += 1
        print(termo)