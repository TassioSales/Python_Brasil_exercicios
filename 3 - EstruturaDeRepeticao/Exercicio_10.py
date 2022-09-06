"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles."""

def main():
    """Função principal"""
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i, end=' ')
    else:
        for i in range(numero2 + 1, numero1):
            print(i, end=' ')


if __name__ == '__main__':
    main()