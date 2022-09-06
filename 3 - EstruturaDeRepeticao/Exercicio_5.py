'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.'''

def crescimento_populacional():
    while True:
        try:
            pop_a = int(input('Digite a população A: '))
            pop_b = int(input('Digite a população B: '))
            taxa_a = float(input('Digite a taxa de crescimento da população A: '))
            taxa_b = float(input('Digite a taxa de crescimento da população B: '))
            anos = 0
            while pop_a < pop_b:
                pop_a += pop_a * taxa_a
                pop_b += pop_b * taxa_b
                anos += 1
            return anos
        except ValueError:
            print('Valores inválidos!')

if __name__ == '__main__':
    anos = crescimento_populacional()
    print(f'População A ultrapassa a população B em {anos} anos.')