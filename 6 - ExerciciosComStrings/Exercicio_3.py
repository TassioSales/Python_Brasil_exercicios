"""Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical."""


def lerStrig():
    string = input('Digite seu nome: ')
    return string


def nomeVertical(string):
    for i in string:
        print(i)


def main():
    string = lerStrig()
    nomeVertical(string)


if __name__ == '__main__':
    main()