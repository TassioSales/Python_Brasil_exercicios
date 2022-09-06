"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até
que o valor seja maior que 500."""

def fibonacci():
    """Função que retorna a série de Fibonacci"""
    lista = [0, 1]
    while lista[-1] < 500:
        lista.append(lista[-1] + lista[-2])
    print(lista)

if __name__ == '__main__':
    fibonacci()
