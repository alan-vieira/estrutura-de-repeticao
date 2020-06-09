# 3. Faça um programa que leia e valide as seguintes
# informações:
#
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = ""
idade = 0
salario = 0
sexo = ""
estado_civil = ""

while (len(nome)<=3):
  nome = input("Nome: (com mais de 3 letras) ")

while (idade < 0 or idade > 150):
  idade = input("Idade:(entre 0 e 150) ")

while (salario <= 0):
  salario = float(input("Salário: (maior que 0) "))

while (sexo != "f" and sexo != "m"):
  sexo = input("Sexo: [m/f] ")

while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
  estado_civil = input("Estado Civil: [s/c/v/d] ")