"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""


def media_alunos():
    """Função que calcula a média de alunos por turma"""
    soma = 0
    quantidade = int(input('Quantas turmas deseja calcular a média de alunos? '))
    for i in range(1, quantidade + 1):
        alunos = int(input(f'Digite a quantidade de alunos da {i}ª turma: '))
        if alunos > 40:
            print('A turma não pode ter mais de 40 alunos')
            break
        soma += alunos
    media = soma / quantidade
    print(f'A média de alunos por turma é {media}')


if __name__ == '__main__':
    media_alunos()
