"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""

#função para criar um vetor com 10 numeros aleatorios
def criavetorrandomico():
    import random
    listaNumeros = []
    for i in range(10):
        listaNumeros.append(random.randint(0,1000))
    return listaNumeros

#função para concatenar dois vetores e intercalar os elementos
def intercalarVetores(vetor1, vetor2, vetor3):
    vetor4 = []
    for i in range(len(vetor1)):
        vetor4.append(vetor1[i])
        vetor4.append(vetor2[i])
        vetor4.append(vetor3[i])
    return vetor4


def main():
    listaNumeros1 = criavetorrandomico()
    listaNumeros2 = criavetorrandomico()
    listaNumeros3 = criavetorrandomico()
    
    print(f"Lista de numeros 1: {listaNumeros1}")
    print(f"Lista de numeros 2: {listaNumeros2}")
    print(f"Lista de numeros 3: {listaNumeros3}")
    print(f"Lista de numeros 4: {intercalarVetores(listaNumeros1, listaNumeros2, listaNumeros3)}")
    
    
if __name__ == '__main__':
    main()