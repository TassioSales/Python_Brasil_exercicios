"""Faça um programa que leia 5 números e informe o maior número."""


def maior_numero():
    """Função que retorna o maior número"""
    maior = 0
    for i in range(5):
        numero = int(input('Digite um número: '))
        if numero > maior:
            maior = numero
    return maior


def maiorNumero():
    """Função que retorna o maior número"""
    lista = []
    for i in range(5):
        numero = int(input('Digite um número: '))
        lista.append(numero)
    return max(lista)


if __name__ == '__main__':
    print(f"O maior numero digitado foi {maior_numero()}")
    print(f"O maior numero digitado foi {maiorNumero()}")
