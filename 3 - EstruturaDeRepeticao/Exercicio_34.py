"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo."""

def primo():
    """Função que verifica se um número é primo"""
    numero = int(input('Digite um número: '))
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        print(f'O número {numero} é primo')
        print(f'{numero} é divisível por {contador} números')
    else:
        print(f'O número {numero} não é primo')
        print(f'{numero} é divisível por {contador} números')

if __name__ == '__main__':
    primo()
