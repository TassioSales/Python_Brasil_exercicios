"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""


def main():
    """Função principal"""
    lista = []
    while True:
        numero = int(input('Digite um número: '))
        if numero == 0:
            break
        lista.append(numero)
    print(f'Menor valor: {min(lista)}')
    print(f'Maior valor: {max(lista)}')
    print(f'Soma dos valores: {sum(lista)}')


if __name__ == '__main__':
    main()
