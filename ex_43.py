# 43. O cardápio de uma lanchonete é o seguinte:
#
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
#
# Faça um programa que leia o código dos itens
# pedidos e as quantidades desejadas. Calcule
# e mostre o valor a ser pago por item
# (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando
# o pedido deve ser encerrado.


while (True):
    soma = 0
    codigo = 1
    cont = 1
    print()
    print("------------------------")
    print("Lanchonete")
    print("------------------------")
    while(codigo != 0):
        codigo = float(input("Informe o código {}: ".format(cont)))
        quantidade = float(input("Informe a quantidade: "))
        print()

        # pedido
        if (codigo == 100):
            pedido = 1.20 * quantidade
            soma += pedido

        if (codigo == 101):
            pedido = 1.30 * quantidade
            soma += pedido

        if (codigo == 102):
            pedido = 1.50 * quantidade
            soma += pedido

        if (codigo == 103):
            pedido = 1.20 * quantidade
            soma += pedido

        if (codigo == 104):
            pedido = 1.30 * quantidade
            soma += pedido

        if (codigo == 105):
            pedido = 1.00 * quantidade
            soma += pedido

        cont += 1

    else:
        quantidade = 0
        print("------------------------")
        print("Total: R$",round(soma,3))

    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$",round(dinheiro - soma,3))
    print("------------------------")
    break