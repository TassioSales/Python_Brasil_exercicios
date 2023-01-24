"""Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete
uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os
iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois,
faça um programa que peça uma texto e transforme-o para a grafia leet speak."""


def lerTexto():
    try:
        texto = input('Digite um texto: ')
        return texto
    except ValueError:
        print('Digite um texto válido.')
        return lerTexto()
    except Exception as e:
        print(e)
        return lerTexto()


def traduzLeet(texto):
    texto = texto.lower()
    texto = texto.replace('a', '4')
    texto = texto.replace('e', '3')
    texto = texto.replace('i', '1')
    texto = texto.replace('o', '0')
    texto = texto.replace('s', '5')
    return texto


def main():
    texto = lerTexto()
    texto = traduzLeet(texto)
    print(texto)


if __name__ == '__main__':
    main()