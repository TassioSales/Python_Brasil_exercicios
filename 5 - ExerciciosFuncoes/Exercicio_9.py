"Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721"


def pede_numero():
    numero = int(input("Digite um número: "))
    return numero


def inverte_numero(numero):
    numero_invertido = str(numero)[::-1]
    return numero_invertido


def main():
    numero = pede_numero()
    numero_invertido = inverte_numero(numero)
    print(numero_invertido)


if __name__ == "__main__":
    main()
