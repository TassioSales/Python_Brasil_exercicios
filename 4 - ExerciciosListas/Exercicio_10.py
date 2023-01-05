"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

#função para criar um vetor com 10 numeros aleatorios
def criavetorrandomico():
    import random
    listaNumeros = []
    for i in range(10):
        listaNumeros.append(random.randint(0,1000))
    return listaNumeros

#função para concatenar dois vetores e intercalar os elementos
def intercalarVetores(vetor1, vetor2):
    vetor3 = []
    for i in range(len(vetor1)):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
    return vetor3

def main():
    listaNumeros1 = criavetorrandomico()
    listaNumeros2 = criavetorrandomico()
    
    print(f"Lista de numeros 1: {listaNumeros1}")
    print(f"Lista de numeros 2: {listaNumeros2}")
    print(f"Lista de numeros 3: {intercalarVetores(listaNumeros1, listaNumeros2)}")

    
if __name__ == '__main__':
    main()