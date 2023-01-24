"""Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada."""


def lerStrig():
    string = input('Digite seu nome: ')
    return string


def nomeVertical(string):
    for i in range(len(string)):
        print(string[:i + 1])


def main():
    string = lerStrig()
    nomeVertical(string)


if __name__ == '__main__':
    main()
