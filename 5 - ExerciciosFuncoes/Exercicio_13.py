"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função
deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
forma elegante."""

import sys


def pedeLinhasEColunas():
    try:
        linhas = int(input("Digite o número de linhas: "))
        colunas = int(input("Digite o número de colunas: "))
        if linhas < 1 or linhas > 20:
            raise ValueError
        elif colunas < 1 or colunas > 20:
            raise ValueError
        return linhas, colunas
    except ValueError:
        print("Digite um número válido.")
        return pedeLinhasEColunas()
    except Exception as e:
        print(e)
        return pedeLinhasEColunas()


def desenhaMoldura(linhas, colunas):
    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            print("+", end="")
            for j in range(colunas):
                print("-", end="")
            print("+")
        else:
            print("|", end="")
            for j in range(colunas):
                print(" ", end="")
            print("|")


def main():
    linhas, colunas = pedeLinhasEColunas()
    desenhaMoldura(linhas, colunas)


if __name__ == "__main__":
    main()
