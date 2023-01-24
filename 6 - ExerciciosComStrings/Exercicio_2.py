"""Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
usuário pode digitar letras maiúsculas ou minúsculas."""


def lerNome():
    nome = input('Digite seu nome: ')
    return nome


def nomeContrario(nome):
    print(nome[::-1].upper())


def main():
    nome = lerNome()
    nomeContrario(nome)


if __name__ == '__main__':
    main()
