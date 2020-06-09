# 4. Supondo que a população de um país A seja da ordem de
# 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma
# taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a
# população do país B, mantidas as taxas de crescimento.

pais_a = 80000
pais_b = 200000
taxa_a = 3
taxa_b = 1.5
ano = 0

while(pais_a <= pais_b):
    ano += 1
    pais_a = (pais_a + ((pais_a * taxa_a) / 100))
#    print("País A: ",pais_a)

    pais_b = (pais_b + ((pais_b * taxa_b) / 100))

print("País A:",round(pais_a),"habitantes", "e País B:",round(pais_b),"habitantes")
print(ano,"anos")