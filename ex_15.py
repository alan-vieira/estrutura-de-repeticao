# 15. A série de Fibonacci é formada pela seqüência
# 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz
# de gerar a série até o n−ésimo termo.

n = int(input("Informe a quantidade de termos da sequência: "))
ultimo = 0
penultimo = 1

if (n == 1 or n == 2):
    print("1")
else:
    cont = 2
    while(cont <= (n+1)):
        termo = ultimo + penultimo
        penultimo, ultimo = ultimo, termo
        cont += 1
        print(termo)
