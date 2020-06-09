# 11. Altere o programa anterior para mostrar no final
# a soma dos números.

num1 = int(input("Digite primeiro número do intervalo: "))
num2 = int(input("Digite último número do intervalo: "))
soma = 0
for i in (range(num1,num2,1)):
    soma += i
    print(i,end=" ")
print()
print("A soma dos números é igual a: ",soma)