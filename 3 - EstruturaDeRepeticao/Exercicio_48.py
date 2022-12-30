"""Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321"""
  
  
def pedenumero():
    numero = int(input('Digite um número inteiro positivo: '))
    return numero

def invertenumero(numero):
    numero = str(numero)
    numero = numero[::-1]
    return numero

def main():
    numero = pedenumero()
    numero = invertenumero(numero)
    print(numero)
    
if __name__ == '__main__':
    main()