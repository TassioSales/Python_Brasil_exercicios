"""Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para
que ele mostre os números um ao lado do outro."""


def main():
    """Função principal"""
    for i in range(1, 21):
        print(i)

    print('  ', end=' ')

    for i in range(1, 21):
        print(i, end=' ')


if __name__ == '__main__':
    main()
