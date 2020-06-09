# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um
# programa que calcule o valor de H com N termos.


s = []
n = 1
m = 1

termos = int(input("Digite o número de termos da série: "))
print("H = ",end="")

for i in range(termos):
    s.append(n/m)
    print("1/{} + ".format(m),end="")
    m += 1
soma = sum(s)

print()
print("H = {}".format(round(soma,2)))
