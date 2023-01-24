"Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."


def pedeNumero():
    numero = int(input("Digite um número inteiro: "))
    return numero


def contaDigito(numero):
    cont = 0
    numero = str(numero)
    for num in numero:
        cont += 1
    return cont


def main():
    numero = pedeNumero()
    cont = contaDigito(numero)
    print("O número %d tem %d dígitos." % (numero, cont))


if __name__ == "__main__":
    main()
