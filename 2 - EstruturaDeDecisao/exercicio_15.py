"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

r1 = float(input("Primeiro seguimento: "))
r2 = float(input("Segundo seguimento:  "))
r3 = float(input("Terceiro seguimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos {r1}, {r2}, {r3} PODEM FORMA TRIANGULO")
else:
    print(f"Os segmentos {r1}, {r2}, {r3} NAO PODEM FORMA TRIANGULO")