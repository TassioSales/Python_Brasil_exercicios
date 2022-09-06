"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada."""


def media_idade():
    """Função que calcula a média de idade"""
    soma = 0
    quantidade = int(input('Quantas pessoas deseja calcular a média de idade? '))
    for i in range(1, quantidade + 1):
        idade = int(input(f'Digite a idade da {i}ª pessoa: '))
        soma += idade
    media = soma / quantidade
    print(f'A média de idade é {media}')
    if 0 <= media <= 25:
        print('A turma é jovem')
    elif 26 <= media <= 60:
        print('A turma é adulta')
    else:
        print('A turma é idosa')

if __name__ == '__main__':
    media_idade()
