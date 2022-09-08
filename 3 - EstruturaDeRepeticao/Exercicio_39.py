"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas."""


def alturaAlunos():
    print('Digite o número do aluno e sua altura em centímetros')
    alunos = {"Aluno": [], "Altura": []}
    for i in range(10):
        aluno = int(input('Aluno: '))
        altura = float(input('Altura: '))
        alunos['Aluno'].append(aluno)
        alunos['Altura'].append(altura)
    print(f'O aluno mais alto é o {alunos["Aluno"][alunos["Altura"].index(max(alunos["Altura"]))]} com {max(alunos["Altura"])}cm')
    print(f'O aluno mais baixo é o {alunos["Aluno"][alunos["Altura"].index(min(alunos["Altura"]))]} com {min(alunos["Altura"])}cm')


if __name__ == '__main__':
    alturaAlunos()

