"""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""


def lerPalavra():
    try:
        palavra = input('Digite uma palavra: ')
        return palavra
    except ValueError:
        print('Digite uma palavra válida.')
        return lerPalavra()
    except Exception as e:
        print(e)
        return lerPalavra()


def verificaPalindromo(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(' ', '')
    if palavra == palavra[::-1]:
        print('A palavra é um palíndromo.')
    else:
        print('A palavra não é um palíndromo.')


def main():
    palavra = lerPalavra()
    verificaPalindromo(palavra)


if __name__ == '__main__':
    main()
