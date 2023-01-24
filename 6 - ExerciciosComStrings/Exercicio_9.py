"""Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de
formatação."""

import re


def lerCpf():
    try:
        cpf = input('Digite seu CPF: ')
        cpf = re.sub("[^0-9]", '', cpf)
        if len(cpf) != 11:
            raise ValueError
        else:
            return cpf
    except ValueError:
        print('CPF inválido.')
        return lerCpf()
    except Exception as e:
        print(e)
        return lerCpf()


def validaCPF():
    cpf = lerCpf()
    cpf = [int(i) for i in cpf]
    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if digito1 == cpf[9] and digito2 == cpf[10]:
        print('CPF válido.')
    else:
        print('CPF inválido.')


def main():
    validaCPF()


if __name__ == '__main__':
    main()
