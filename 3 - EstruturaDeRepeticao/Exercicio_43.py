"""O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
ser encerrado.
"""

def menu():
    print('Especificação Código Preço')
    print('Cachorro Quente 100 R$ 1,20')
    print('Bauru Simples 101 R$ 1,30')
    print('Bauru com ovo 102 R$ 1,50')
    print('Hambúrguer 103 R$ 1,20')
    print('Cheeseburguer 104 R$ 1,30')
    print('Refrigerante 105 R$ 1,00')

def lanche():
    try:
        menu()
        pedido = int(input('Código do pedido: '))
        quantidade = int(input('Quantidade: '))
        if pedido == 100:
            print(f'Valor a ser pago: R$ {quantidade * 1.20}')
        elif pedido == 101:
            print(f'Valor a ser pago: R$ {quantidade * 1.30}')
        elif pedido == 102:
            print(f'Valor a ser pago: R$ {quantidade * 1.50}')
        elif pedido == 103:
            print(f'Valor a ser pago: R$ {quantidade * 1.20}')
        elif pedido == 104:
            print(f'Valor a ser pago: R$ {quantidade * 1.30}')
        elif pedido == 105:
            print(f'Valor a ser pago: R$ {quantidade * 1.00}')
    except ValueError:
        print('Valor inválido')
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    lanche()
