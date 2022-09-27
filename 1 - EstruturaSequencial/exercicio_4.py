#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

soma = nota_1 + nota_2 + nota_3 + nota_4

media =  soma / 4

print(f"A media obtida foi {media}")