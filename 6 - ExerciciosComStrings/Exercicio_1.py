"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""


def lerStrig():
    global string2, string1
    for i in range(2):
        if i == 0:
            string1 = input('String 1: ')
        else:
            string2 = input('String 2: ')
    return string1, string2


def tamanhoString(string1, string2):
    print('Tamanho de "{}": {} caracteres'.format(string1, len(string1)))
    print('Tamanho de "{}": {} caracteres'.format(string2, len(string2)))


def comparaString(string1, string2):
    if len(string1) == len(string2):
        print('As duas strings são de tamanhos iguais.')
    else:
        print('As duas strings são de tamanhos diferentes.')
    if string1 == string2:
        print('As duas strings possuem conteúdo igual.')
    else:
        print('As duas strings possuem conteúdo diferente.')


def main():
    lerStrig()
    tamanhoString(string1, string2)
    comparaString(string1, string2)


if __name__ == '__main__':
    main()
