"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
 não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
 usuário, conforme exemplo abaixo:"""


def tabuada():
    """Função que calcula a tabuada de um número inteiro"""
    while True:
        numero = int(input('Digite um número: '))
        inicio = int(input('Digite o início da tabuada: '))
        fim = int(input('Digite o fim da tabuada: '))
        if inicio < fim:
            for i in range(inicio, fim + 1):
                print(f'{numero} x {i} = {numero * i}')
        else:
            print('O início da tabuada deve ser menor que o fim')
        continuar = input('Deseja continuar? [S/N] ').upper().split()[0]
        if continuar == 'N':
            break


if __name__ == '__main__':
    tabuada()
