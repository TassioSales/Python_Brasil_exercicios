"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

def dadosAtleta():
    nome = input("Qual o nome do atleta? ")
    saltos = []
    for salto in range(5):
        salto = float(input("Qual a distância do salto? "))
        saltos.append(salto)
    return nome, saltos

def calculaMedia(saltos):
    media = sum(saltos) / len(saltos)
    return media

def main():
    nome, saltos = dadosAtleta()
    media = calculaMedia(saltos)
    print(f"Resultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}")
    print(f"Média dos saltos: {media:.2f} m")
    
if __name__ == '__main__':
    main()
        