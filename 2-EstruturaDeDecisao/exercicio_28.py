"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""


def menu():
    print("#### Carnes ####")
    print()
    print("1 - File Duplo")
    print("2 - Alcatra")
    print("3 - Picanha")
    print()
    print("0 - Sair")
    print()
    return int(input("Qual carne deseja comprar: "))


def MenuFormasPagamento():
    print("#### Formas de Pagamento ####")
    print()
    print("1 - Cartão Tabajara")
    print("2 - Cartão Credito")
    print("3 - Cartão Débito")
    print("2 - Dinheiro")
    print()
    return int(input("Qual forma de pagamento deseja utilizar: "))


def calculaPreco(tipo, quantidade, formaPagamento):
    if tipo == 1:
        preco = 4.90 * quantidade
    elif tipo == 2:
        preco = 5.90 * quantidade
    elif tipo == 3:
        preco = 6.90 * quantidade
    else:
        preco = 0

    if formaPagamento == 1:
        desconto = preco - (preco * 5 / 100)
    else:
        desconto = 0
    return preco, desconto

if __name__ == '__main__':
    while True:
        opcao = menu()
        if opcao == 0:
            break
        quantidade = int(input("Quantidade: "))
        formaPagamento = MenuFormasPagamento()
        preco, desconto = calculaPreco(opcao, quantidade, formaPagamento)
        print("Preço: R$ {:.2f}".format(preco))
        print("Desconto: R$ {:.2f}".format(desconto))
        print("Total a pagar: R$ {:.2f}".format(preco - desconto))
        print()
        print("#### Fim da Compra ####")
        print()
        print("#### Cupom Fiscal ####")
        print()
        print("Tipo de carne: {}".format("File Duplo" if opcao == 1 else "Alcatra" if opcao == 2 else "Picanha" if opcao == 3 else "Nenhuma"))
        print("Quantidade: {} Kilos".format(quantidade))
        print("Preço: R$ {:.2f}".format(preco))
        print("Desconto: R$ {:.2f}".format(desconto))
        print("Total a pagar: R$ {:.2f}".format(preco - desconto))
        print()
        print("#### Fim da Compra ####")
        print()
        print("#### Cupom Fiscal ####")
        print()
        print("Tipo de carne: {}".format("File Duplo" if opcao == 1 else "Alcatra" if opcao == 2 else "Picanha" if opcao == 3 else "Nenhuma"))
        print("Quantidade: {} Kilos".format(quantidade))
        print("Preço: R$ {:.2f}".format(preco))
        print("Desconto: R$ {:.2f}".format(desconto))
        print("Total a pagar: R$ {:.2f}".format(preco - desconto))