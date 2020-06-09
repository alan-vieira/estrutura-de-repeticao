# 20. Altere o programa de cálculo do fatorial, permitindo
# ao usuário calcular o fatorial várias vezes e limitando
# o fatorial a números inteiros positivos e menores
# que 16.

n = int(input("Informe o n fatorial: "))
fatorial = 1

for i in (range(1,(n + 1))):
    fatorial *= i
    print(i,end=" ")
print()
print(n,"! =",fatorial)
