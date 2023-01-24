"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso
deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

import re


def lerTelefone():
    try:
        telefone = input('Digite seu telefone: ')
        telefone = re.sub("[^0-9]", '', telefone)
        if len(telefone) != 7 and len(telefone) != 8:
            raise ValueError
        else:
            return telefone
    except ValueError:
        print('Telefone inválido.')
        return lerTelefone()
    except Exception as e:
        print(e)
        return lerTelefone()


def validaTelefone():
    telefone = lerTelefone()
    if len(telefone) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        telefone = '3' + telefone
    print('Telefone corrigido sem formatação: {}'.format(telefone))
    print('Telefone corrigido com formatação: {}-{}'.format(telefone[:4], telefone[4:]))


def main():
    validaTelefone()


if __name__ == '__main__':
    main()