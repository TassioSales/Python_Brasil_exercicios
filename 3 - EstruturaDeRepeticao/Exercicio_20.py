"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16."""


def fatorial():
    """Função que retorna o fatorial de um número"""
    while True:
        numero = int(input('Digite um número: '))
        if numero < 0 or numero > 16:
            print('Número inválido')
            continue
        fatorial = 1
        for i in range(1, numero + 1):
            print(i, end=' x ' if i < numero else ' = ')
            fatorial *= i
        print(fatorial)
        if input('Deseja continuar? [S/N] ').upper().split()[0] == 'N':
            break


if __name__ == '__main__':
    fatorial()