"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

def lervetor(vetor):
    # Invertendo a ordem do vetor
    vetor.reverse()
    for item in vetor:
        print(item, end=" ")
        
vetor = [1,2,3,4,5,6,7,8,9,10]

lervetor(vetor)