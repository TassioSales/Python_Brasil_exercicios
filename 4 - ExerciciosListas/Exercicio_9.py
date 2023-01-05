"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor."""

#função para criar um vetor com 10 numeros aleatorios
def criavetorrandomico():
    import random
    listaNumeros = []
    for i in range(10):
        listaNumeros.append(random.randint(0,1000))
    return listaNumeros

#função para calcular a soma dos quadrados dos elementos do vetor
def somaQuadrados(vetor):
    soma = 0
    for item in vetor:
        soma += item ** 2
    return soma

def main():
    listaNumeros = criavetorrandomico()
    print(f"Lista de numeros: {listaNumeros}")
    print(f"Soma dos quadrados dos elementos do vetor: {somaQuadrados(listaNumeros)}")
    
if __name__ == '__main__':
    main()