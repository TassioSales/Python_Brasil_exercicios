"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""


def lerString():
    try:
        string = input('Digite uma frase: ')
        return string
    except ValueError:
        print('Valor inválido.')
        return lerString()
    except Exception as e:
        print('Erro desconhecido: {}'.format(e))
        return lerString()


def contaEspacos(string):
    espacos = 0
    for i in string:
        if i == ' ':
            espacos += 1
    return espacos


def contaVogais(string):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in string:
        if i in vogais:
            vogais[i] += 1
    return vogais


def mostraResultado(espacos, vogais):
    print('Quantidade de espaços: {}'.format(espacos))
    for i in vogais:
        print('Quantidade de {}: {}'.format(i, vogais[i]))
    print('Quantidade total de vogais: {}'.format(sum(vogais.values())))
    print('Quantidade total de caracteres: {}'.format(sum(vogais.values()) + espacos))


def main():
    string = lerString()
    espacos = contaEspacos(string)
    vogais = contaVogais(string)
    mostraResultado(espacos, vogais)


if __name__ == '__main__':
    main()
