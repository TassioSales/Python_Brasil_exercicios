"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""

def numeros_impares():
    """Função que retorna os números ímpares"""
    for i in range(1, 51, 2):
        print(i, end=' ')

def numerosImpares():
    """Função que retorna os números ímpares"""
    lista = []
    for i in range(1, 51):
        if i % 2 != 0:
            lista.append(i)
    for i in lista:
        print(i, end=' ')

if __name__ == '__main__':
    numeros_impares()
    print()
    numerosImpares()
