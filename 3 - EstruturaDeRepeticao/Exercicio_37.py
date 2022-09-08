"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""


def senso():
    """Função que calcula o mais alto, o mais baixo, o mais gordo e o mais magro de uma academia"""
    codigos = []
    alturas = []
    pesos = []
    while True:
        codigo = int(input('Digite o código do cliente: '))
        if codigo == 0:
            break
        altura = float(input('Digite a altura do cliente: '))
        peso = float(input('Digite o peso do cliente: '))
        codigos.append(codigo)
        alturas.append(altura)
        pesos.append(peso)
        opt = input('Deseja continuar? [S/N] ').upper().split()[0]
        if opt == 'N':
            break
    print(f'O cliente mais alto é o {codigos[alturas.index(max(alturas))]} com {max(alturas)}m')
    print(f'O cliente mais baixo é o {codigos[alturas.index(min(alturas))]} com {min(alturas)}m')
    print(f'O cliente mais gordo é o {codigos[pesos.index(max(pesos))]} com {max(pesos)}kg')
    print(f'O cliente mais magro é o {codigos[pesos.index(min(pesos))]} com {min(pesos)}kg')
    print(f'A média das alturas é {sum(alturas) / len(alturas)}m')
    print(f'A média dos pesos é {sum(pesos) / len(pesos)}kg')




if __name__ == '__main__':
    senso()

