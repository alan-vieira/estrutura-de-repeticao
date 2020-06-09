# 10. Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo
# compreendido por eles.

num1 = int(input("Digite primeiro número do intervalo: "))
num2 = int(input("Digite último número do intervalo: "))
for i in (range(num1,num2,1)):
    print(i,end=" ")