"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
# Importando a biblioteca random
import random

#criar função para gerar numeros aleatórios
def gerar():
    return random.randint(1,6)

#criar para jogar o dado 100 vezes  e armazene os resultados em um vetor
def jogar():
    vetor = []
    for i in range(10000):
        vetor.append(gerar())
    return vetor

#criar função para contar quantas vezes cada valor foi conseguido
def contar(vetor):
    cont = [0,0,0,0,0,0]
    for i in range(len(vetor)):
        if vetor[i] == 1:
            cont[0] += 1
        elif vetor[i] == 2:
            cont[1] += 1
        elif vetor[i] == 3:
            cont[2] += 1
        elif vetor[i] == 4:
            cont[3] += 1
        elif vetor[i] == 5:
            cont[4] += 1
        elif vetor[i] == 6:
            cont[5] += 1
    return cont


#criar função para mostrar quantas vezes cada valor foi conseguido
def mostrar(cont):
    print("O valor 1 foi conseguido %d vezes" %cont[0])
    print("O valor 2 foi conseguido %d vezes" %cont[1])
    print("O valor 3 foi conseguido %d vezes" %cont[2])
    print("O valor 4 foi conseguido %d vezes" %cont[3])
    print("O valor 5 foi conseguido %d vezes" %cont[4])
    print("O valor 6 foi conseguido %d vezes" %cont[5])
    
    
#criar função principal
def main():
    vetor = jogar()
    cont = contar(vetor)
    mostrar(cont)
    
    
#chamar função principal
if __name__ == '__main__':
    main()