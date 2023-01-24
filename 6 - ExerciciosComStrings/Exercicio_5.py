"""Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida."""


def lerStrig():
    string = input('Digite seu nome: ')
    return string


def nomeVertical(string):
    for i in range(len(string)):
        print(string[i:])


def main():
    string = lerStrig()
    nomeVertical(string)


if __name__ == '__main__':
    main()
