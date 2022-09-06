"""Altere o programa anterior para mostrar no final a soma dos números."""


def main():
    """Função principal"""
    soma = 0
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i, end=' ')
            soma += i
    else:
        for i in range(numero2 + 1, numero1):
            print(i, end=' ')
            soma += i
    print(f"\nA soma dos números é, {soma}")


if __name__ == '__main__':
    main()
