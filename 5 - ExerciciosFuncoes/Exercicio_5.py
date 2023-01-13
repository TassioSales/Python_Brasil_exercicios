"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def pedevalor():
    taxaDeimposto = float(input("Digite a taxa de imposto: "))
    custo = float(input("Digite o custo: "))
    return taxaDeimposto, custo

def calculaImposto(taxaDeimposto, custo):
    imposto = (taxaDeimposto / 100) * custo
    custo += imposto
    return custo


def main():
    taxaDeimposto, custo = pedevalor()
    custo = calculaImposto(taxaDeimposto, custo)
    print(custo)
    
if __name__ == "__main__":
    main()  