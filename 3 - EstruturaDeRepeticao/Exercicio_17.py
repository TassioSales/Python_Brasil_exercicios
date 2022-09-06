"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

def fatorial():
    """Função que retorna o fatorial de um número"""
    numero = int(input('Digite um número: '))
    fatorial = 1
    for i in range(1, numero + 1):
        print(i, end=' x ' if i < numero else ' = ')
        fatorial *= i
    print(fatorial)

if __name__ == '__main__':
    fatorial()