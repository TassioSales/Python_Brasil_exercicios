"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""


def numero_primo():
    """Função que retorna se um número é primo ou não"""
    numero = int(input('Digite um número: '))
    for i in range(2, numero):
        if numero % i == 0:
            print(f'{numero} não é primo')
            print(f'{numero} é divisível por {i}')
            break
    else:
        print(f'{numero} é primo')


if __name__ == '__main__':
    numero_primo()
