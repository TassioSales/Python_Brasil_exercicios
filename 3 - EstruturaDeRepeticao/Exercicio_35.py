"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário."""


def primo():
    """Função que verifica se um número é primo"""
    numero = int(input('Digite um número: '))
    num = []
    for i in range(1, numero + 1):
        contador = 0
        for j in range(1, i + 1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            num.append(i)
    print(f'Os números primos entre 1 e {numero} são: {num}')


if __name__ == '__main__':
    primo()
