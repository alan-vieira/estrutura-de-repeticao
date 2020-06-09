# 49. Faça um programa que mostre os n termos da Série
# a seguir:
#
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.


s = []
n = 1
m = 1

termos = int(input("Digite o enézimo termo da série: "))
print("S = ",end="")

for i in range(termos):
    s.append(n/m)
    print("{}/{} + ".format(n,m),end="")
    n += 1
    m += 2
soma = sum(s)

print()
print("S = {}".format(round(soma,2)))
