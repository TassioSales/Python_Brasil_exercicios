"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def pedenumero():
    n = int(input("Digite um número: "))
    return n

def positivoOuNegativo(n):
    if n > 0:
        return "P"
    else:
        return "N"
    
def main():
    n = pedenumero()
    resultado = positivoOuNegativo(n)
    print(resultado)
    
if __name__ == "__main__":
    main()