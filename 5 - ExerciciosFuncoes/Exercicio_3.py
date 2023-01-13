"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""

def pedevalor():
    lista = []
    for i in range(3):
        n = int(input("Digite um número: "))
        lista.append(n)
    return lista

def somaLista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def main():
    lista = pedevalor()
    soma = somaLista(lista)
    print(soma)
    
if __name__ == "__main__":
    main()