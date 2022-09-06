"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares."""


def impares_pares():
    """Função que retorna a quantidade de números pares e ímpares"""
    pares = 0
    impares = 0
    for i in range(10):
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f'Quantidade de números pares: {pares}')
    print(f'Quantidade de números ímpares: {impares}')


def imparesPares():
    """Função que retorna a quantidade de números pares e ímpares"""
    lista = []
    for i in range(10):
        numero = int(input('Digite um número: '))
        lista.append(numero)
    print(f'Numero pares: {list(filter(lambda x: x % 2 == 0, lista))}')
    print(f'Quantidade de números pares: {len([i for i in lista if i % 2 == 0])}')
    print(f'Numero impares: {list(filter(lambda x: x % 2 != 0, lista))}')
    print(f'Quantidade de números ímpares: {len([i for i in lista if i % 2 != 0])}')


def imparesPares2():
    """Função que retorna a quantidade de números pares e ímpares"""
    listaPar = []
    listaImpar = []
    for i in range(10):
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    print(f'Numero pares: {listaPar}')
    print(f'Quantidade de números pares: {len(listaPar)}')
    print(f'Numero impares: {listaImpar}')
    print(f'Quantidade de números ímpares: {len(listaImpar)}')


if __name__ == '__main__':
    imparesPares2()
