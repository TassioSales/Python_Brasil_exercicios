"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual
a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as
características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada
quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3."""

from itertools import permutations


def quadrado_magico():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in permutations(numeros):
        if i[0] + i[1] + i[2] == i[3] + i[4] + i[5] == i[6] + i[7] + i[8] == i[0] + i[3] + i[6] == i[1] + i[4] + i[7] == \
                i[2] + i[5] + i[8] == i[0] + i[4] + i[8] == i[2] + i[4] + i[6]:
            print(f"{i[0]} {i[1]} {i[2]} sum: {i[0] + i[1] + i[2]}")
            print(f"{i[3]} {i[4]} {i[5]} sum: {i[3] + i[4] + i[5]}")
            print(f"{i[6]} {i[7]} {i[8]} sum: {i[6] + i[7] + i[8]}")
            print()


def main():
    quadrado_magico()


if __name__ == "__main__":
    main()
