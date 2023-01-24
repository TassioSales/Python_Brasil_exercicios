"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os
carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer
outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em
caixa alta ou caixa baixa, independentemente de como foram digitados."""

import random


def pedePalavra():
    try:
        palavra = input("Digite uma palavra: ")
        if palavra.isalpha():
            return palavra
        else:
            raise ValueError
    except ValueError:
        print("Digite uma palavra válida.")
        return pedePalavra()
    except Exception as e:
        print(e)
        return pedePalavra()


def embaralhaPalavra(palavra):
    palavra = list(palavra)
    random.shuffle(palavra)
    return "".join(palavra)


def main():
    palavra = pedePalavra()
    palavra = embaralhaPalavra(palavra)
    print(palavra)


if __name__ == "__main__":
    main()
