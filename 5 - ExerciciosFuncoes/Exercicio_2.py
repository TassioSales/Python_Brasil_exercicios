"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

"""


def pedevalor():
    n = int(input("Digite um número: "))
    return n


def imprime(n):
    for i in range(1, n + 1):
        print(i * str(i))


def main():
    n = pedevalor()
    imprime(n)


if __name__ == "__main__":
    main()
