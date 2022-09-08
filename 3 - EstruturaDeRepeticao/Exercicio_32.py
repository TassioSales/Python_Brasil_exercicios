"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:"""


def fatorial():
    """Função que calcula o fatorial de um número inteiro"""
    numero = int(input('Digite um número: '))
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f'{numero}! = {fatorial}')


if __name__ == '__main__':
    fatorial()
