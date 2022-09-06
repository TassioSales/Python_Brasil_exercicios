"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""


def colecao_cd():
    """Função que calcula o valor total investido e o valor médio gasto em cada CD"""
    soma = 0
    quantidade = int(input('Quantos CDs deseja calcular o valor total investido? '))
    for i in range(1, quantidade + 1):
        valor = float(input(f'Digite o valor do {i}º CD: '))
        soma += valor
    media = soma / quantidade
    print(f'O valor total investido é {soma}')
    print(f'O valor médio gasto em cada CD é {media}')


if __name__ == '__main__':
    colecao_cd()
