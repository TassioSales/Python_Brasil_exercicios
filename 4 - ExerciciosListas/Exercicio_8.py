"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""

#funçao para pedir a idade e altura de 5 pessoas
def idadeAltura():
    listaIdade = []
    listaAltura = []
    for i in range(5):
        try:
            idade = int(input(f"Digite a idade da pessoa {i+1}: "))
            altura = float(input(f"Digite a altura da pessoa {i+1}: "))
            listaIdade.append(idade)
            listaAltura.append(altura)
        except Exception as e:
            print(f"Erro: {e}")
    return listaIdade, listaAltura

#função para imprimir a idade e altura na ordem inversa
def imprimeInverso(listaIdade, listaAltura):
    print("Idade e altura na ordem inversa:")
    for i in range(4,-1,-1):
        print(f"Idade: {listaIdade[i]} Altura: {listaAltura[i]}")
        
def main():
    listaIdade, listaAltura = idadeAltura()
    imprimeInverso(listaIdade, listaAltura)
    
if __name__ == '__main__':
    main()