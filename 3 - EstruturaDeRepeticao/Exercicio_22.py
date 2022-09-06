"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível."""

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