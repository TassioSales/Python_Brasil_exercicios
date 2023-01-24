"""Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na
tela por extenso."""


def lerNumero():
    try:
        numero = int(input('Digite um número até 99: '))
        if numero < 0 or numero > 99:
            raise ValueError
        return numero
    except ValueError:
        print('Número inválido.')
        return lerNumero()
    except Exception as e:
        print('Erro desconhecido: {}'.format(e))
        return lerNumero()


def numeroExtenso(numero):
    def unidade(numero):
        unidades = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito',
                    9: 'nove'}
        return unidades[numero]

    def dezena(numero):
        dezenas = {10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis',
                   17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta',
                   50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa'}
        return dezenas[numero]

    if numero < 10:
        print(unidade(numero))
    elif numero < 20:
        print(dezena(numero))
    else:
        print('{} e {}'.format(dezena(numero // 10 * 10), unidade(numero % 10)))


def main():
    numero = lerNumero()
    numeroExtenso(numero)


if __name__ == '__main__':
    main()
