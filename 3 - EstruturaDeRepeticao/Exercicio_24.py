"""Faça um programa que calcule o mostre a média aritmética de N notas."""

def media_aritmetica():
    """Função que calcula a média aritmética"""
    soma = 0
    quantidade = int(input('Quantas notas deseja calcular a média? '))
    for i in range(1, quantidade + 1):
        nota = float(input(f'Digite a {i}ª nota: '))
        soma += nota
    media = soma / quantidade
    print(f'A média aritmética é {media}')

if __name__ == '__main__':
    media_aritmetica()

