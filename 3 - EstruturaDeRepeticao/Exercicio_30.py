"""O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:"""


def tabela_precos():
    """Função que monta a tabela de preços"""
    preco = float(input('Digite o preço do pão: '))
    print('Tabela de Preços')
    for i in range(1, 51):
        print(f'{i} - R$ {i * preco:.2f}')

if __name__ == '__main__':
    tabela_precos()