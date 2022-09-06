"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1."""

def numero_primo():
    """Função que retorna se um número é primo ou não"""
    numero = int(input('Digite um número: '))
    for i in range(2, numero):
        if numero % i == 0:
            print(f'{numero} não é primo')
            break
    else:
        print(f'{numero} é primo')

if __name__ == '__main__':
    numero_primo()