"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

def main():
    notas = []
    while True:
        nota = float(input('Digite uma nota: '))
        if nota == -1:
            break
        notas.append(nota)
    print(f'Foram digitadas {len(notas)} notas')
    print('Notas digitadas: ', end='')
    for nota in notas:
        print(nota, end=' ')
    print()
    print('Notas digitadas na ordem inversa: ')
    for nota in notas[::-1]:
        print(nota)
    print()
    print('Soma das notas: ', sum(notas))
    print('Média das notas: ', sum(notas) / len(notas))
    print('Quantidade de notas acima da média: ', len([nota for nota in notas if nota > sum(notas) / len(notas)]))
    print('Quantidade de notas abaixo de 7: ', len([nota for nota in notas if nota < 7]))
    print('Fim do programa')
    
    
if __name__ == '__main__':
    main()
    
        
        