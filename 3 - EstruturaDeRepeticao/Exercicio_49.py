"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""
def serie(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i / (2 * i - 1)
    return soma

def main():
    n = int(input('Digite o valor de n: '))
    print(f'A soma da série é: {serie(n)}')
    
    
if __name__ == '__main__':
    main()