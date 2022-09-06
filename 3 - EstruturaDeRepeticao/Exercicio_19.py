"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""


def main():
    """Função principal"""
    lista = []
    while True:
        numero = int(input('Digite um número: '))
        if numero > 1000 or numero < 0:
            print('Número inválido!')
            continue
        lista.append(numero)
        opt = input('Deseja continuar? [S/N] ').upper().split()[0]
        if opt == 'N':
            break
    print(f'Menor valor: {min(lista)}')
    print(f'Maior valor: {max(lista)}')
    print(f'Soma dos valores: {sum(lista)}')


if __name__ == '__main__':
    main()
