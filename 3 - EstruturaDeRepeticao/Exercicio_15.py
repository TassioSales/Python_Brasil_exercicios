"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
até o n−ésimo termo."""


def fibonacci():
    """Função que retorna a série de Fibonacci"""
    n = int(input('Digite um número: '))
    lista = [1, 1]
    for i in range(2, n):
        lista.append(lista[i - 1] + lista[i - 2])
    print(lista)


if __name__ == '__main__':
    fibonacci()
