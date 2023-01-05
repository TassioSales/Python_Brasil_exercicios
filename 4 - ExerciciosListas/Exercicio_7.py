"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

def soma(vetor):
    soma = 0
    for item in vetor:
        soma += item
    return soma

def multiplicacao(vetor):
    multiplicacao = 1
    for item in vetor:
        multiplicacao *= item
    return multiplicacao

def criavetorrandomico():
    import random
    listaNumeros = []
    for i in range(5):
        listaNumeros.append(random.randint(0,100))
    return listaNumeros

def main():
    listaNumeros = criavetorrandomico()
    print(f"Lista de numeros: {listaNumeros}")
    print(f"Soma: {soma(listaNumeros)}")
    print(f"Multiplicacao: {multiplicacao(listaNumeros)}")
    
    
if __name__ == '__main__':
    main()