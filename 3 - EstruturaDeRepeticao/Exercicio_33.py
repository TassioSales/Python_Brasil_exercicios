"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
das temperaturas."""


def temperatura():
    """Função que calcula a menor, maior e média de temperaturas"""
    temperaturas = []
    while True:
        temperatura = float(input('Digite a temperatura: '))
        temperaturas.append(temperatura)
        opt = input('Deseja continuar? [S/N] ').upper()
        if opt == 'N':
            break
    print(f'A menor temperatura é {min(temperaturas)}')
    print(f'A maior temperatura é {max(temperaturas)}')
    print(f'A média das temperaturas é {sum(temperaturas) / len(temperaturas)}')


if __name__ == '__main__':
    temperatura()
