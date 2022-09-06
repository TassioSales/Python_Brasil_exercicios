"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato"""

def eleicao():
    """Função que calcula a quantidade de votos de cada candidato"""
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0

    print("MENU DE CANDIDATOS")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Voto Nulo")
    print("5 - Voto em Branco")
    quantidade = int(input('Quantos eleitores deseja votar? '))
    for i in range(1, quantidade + 1):
        voto = int(input(f'Digite o voto do {i}º eleitor: '))
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            print('Voto Nulo')
        else:
            print('Voto em Branco')

    print(f'O candidato 1 recebeu {candidato1} votos')
    print(f'O candidato 2 recebeu {candidato2} votos')
    print(f'O candidato 3 recebeu {candidato3} votos')


if __name__ == '__main__':
    eleicao()
