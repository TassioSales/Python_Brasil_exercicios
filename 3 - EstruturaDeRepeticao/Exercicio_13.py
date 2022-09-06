"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número
. Não utilize a função de potência da linguagem"""


def calcula_potencia(base, expoente):
    """Função que calcula a potência"""
    return base ** expoente

if __name__ == '__main__':
    base = int(input('Digite a base: '))
    expoente = int(input('Digite o expoente: '))
    print(f"{base} elevado a {expoente} é {calcula_potencia(base, expoente)}")
