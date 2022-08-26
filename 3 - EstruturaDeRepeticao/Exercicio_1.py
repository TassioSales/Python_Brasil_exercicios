"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido."""

'''while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        break
    print('Nota inválida!')'''


def nota_valida():
    while True:
        try:
            nota = int(input('Digite uma nota entre 0 e 10: '))
            if 0 <= nota <= 10:
                break
        except ValueError:
            print('Nota inválida!')
        else:
            print('Nota inválida!')
    return nota


nota = nota_valida()
print(f'Nota: {nota}')
