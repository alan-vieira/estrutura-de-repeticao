# 5. Altere o programa anterior permitindo ao usuário
# informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input("Favor informar o número de habitantes do país A: "))
pais_b = int(input("Favor informar o número de habitantes do país B: "))
taxa_a = float(input("Favor a taxa de crescimento anual do país A: "))
taxa_b = float(input("Favor a taxa de crescimento anual do país B: "))
ano = 0

while(pais_a <= pais_b):
    ano += 1
    pais_a = (pais_a + ((pais_a * taxa_a) / 100))
#    print("País A: ",pais_a)

    pais_b = (pais_b + ((pais_b * taxa_b) / 100))

print("País A:",round(pais_a),"habitantes", "e País B:",round(pais_b),"habitantes")
print(ano,"anos")