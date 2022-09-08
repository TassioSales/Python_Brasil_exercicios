"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.Os juros e a quantidade de parcelas seguem a tabela abaixo:
"""


def divida():
    juros = [0.05, 0.10, 0.15, 0.20, 0.25]
    parcelas = [1, 3, 6, 9, 12]
    divida = float(input('Valor da dívida: '))
    print('Valor da dívida Valor dos juros Quantidade de parcelas Valor da parcela')
    for i in range(len(juros)):
        print(f'{divida} {divida * juros[i]} {parcelas[i]} {divida * (1 + juros[i]) / parcelas[i]}')


def dividaDois():
    try:
        divida = float(input('Valor da dívida: '))
        parcelas = int(input('Quantidade de parcelas: '))
        juros = 0
        if parcelas == 1:
            juros = 0.05
        elif parcelas == 3:
            juros = 0.10
        elif parcelas == 6:
            juros = 0.15
        elif parcelas == 9:
            juros = 0.20
        elif parcelas == 12:
            juros = 0.25
        print(f'Valor da dívida: {divida}')
        print(f'Valor dos juros: {divida * juros}')
        print(f'Quantidade de parcelas: {parcelas}')
        print(f'Valor da parcela: {divida * (1 + juros) / parcelas}')
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    divida()
    dividaDois()
