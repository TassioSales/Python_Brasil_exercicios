# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:


nota1 = input("Digite a primeira nota: ").replace(',', '.')
nota2 = input("Digite a segunda nota: ").replace(',', '.')
nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1 + nota2) / 2

if media <= 4:
    print(f'Sua nota media foi {media} seu conceito {"E"}')
elif 4 < media <= 6:
    print(f'Sua nota media foi {media} seu conceito {"D"}')
elif 6 < media <= 7.5:
    print(f'Sua nota media foi {media} seu conceito {"C"}')
elif 7.5 < media <= 9:
    print(f'Sua nota media foi {media} seu conceito {"B"}')
elif 9 < media <= 10:
    print(f'Sua nota media foi {media} seu conceito {"A"}')
else:
    print("Sua media esta invalida")
