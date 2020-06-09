# 22. Altere o programa de cálculo dos números primos,
# informando, caso o número não seja primo, por quais
# número ele é divisível.

n = int(input("Digite um número: "))
mult = 0

for count in range(2,n):
    if (n % count == 0):
        print ("Divisível por", count)
        mult += 1
if (mult == 0):
    print ("É primo")