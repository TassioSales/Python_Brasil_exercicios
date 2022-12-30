"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m"""
    
    
def main():
    nome = input('Digite o nome do atleta: ')
    saltos = []
    for i in range(5):
        saltos.append(float(input(f'Digite o {i + 1}º salto: ')))
    #ordena a lista de saltos do maior para o menor
    print(f'Atleta: {nome}')
    
    for i in range(5):
        print(f'{i + 1}º Salto: {saltos[i]} m')
    print()
    
    #pegar o maior e o menor salto
    maior = max(saltos)
    menor = min(saltos)
    print(f'Melhor salto: {maior} m')
    print(f'Pior salto: {menor} m')
    
    #remover o maior e o menor salto
    saltos.remove(maior)
    saltos.remove(menor)
    
    #calcular a média dos saltos
    
    media = sum(saltos) / len(saltos)
    print(f'Média dos demais saltos: {media:.2f} m')
    print()
    
    
    
if __name__ == '__main__':
    main()