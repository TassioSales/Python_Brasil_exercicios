"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
    1 , 2, 3, 4  - Votos para os respectivos candidatos 
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco
    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero"""
    
def menu():
    print('1 - Jose')
    print('2 - João')
    print('3 - Maria')
    print('4 - Joana')
    print('5 - Voto Nulo')
    print('6 - Voto em Branco')
    print('0 - Sair')
    print('')
    opt = int(input('Digite a opção desejada: '))
    return opt

def contavoto(opt):
    jose = 0
    joao = 0
    maria = 0
    joana = 0
    nulo = 0
    branco = 0
    while opt != 0:
        if opt == 1:
            jose += 1
        elif opt == 2:
            joao += 1
        elif opt == 3:
            maria += 1
        elif opt == 4:
            joana += 1
        elif opt == 5:
            nulo += 1
        elif opt == 6:
            branco += 1
        opt = menu()
        
    return jose, joao, maria, joana, nulo, branco

def main():
    jose, joao, maria, joana, nulo, branco = contavoto(menu())
    print(f'Jose: {jose}')
    print(f'João: {joao}')
    print(f'Maria: {maria}')
    print(f'Joana: {joana}')
    print(f'Nulo: {nulo}')
    print(f'Branco: {branco}')
    print(f'Percentual de votos nulos: {nulo / (jose + joao + maria + joana + nulo + branco) * 100}%')
    print(f'Percentual de votos em branco: {branco / (jose + joao + maria + joana + nulo + branco) * 100}%')



    
if __name__ == '__main__':
    main()
    
