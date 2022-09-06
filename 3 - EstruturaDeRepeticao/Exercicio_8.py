"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

def soma_media():
    """Função que retorna a soma e a média dos números"""
    global media
    soma = 0
    for i in range(5):
        numero = int(input('Digite um número: '))
        soma += numero
        media = soma / 5
    print(f"A soma dos números é {soma} e a média é {media}")

    

def somaMedia():
    """Função que retorna a soma e a média dos números"""
    lista = []
    for i in range(5):
        numero = int(input('Digite um número: '))
        lista.append(numero)
    print(f"A soma dos números é {sum(lista)} e a média é {sum(lista) / len(lista)}")

if __name__ == '__main__':
    soma_media()
    somaMedia()

