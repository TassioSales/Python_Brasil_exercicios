#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = C x 1,8 + 32

Celsius = float(input("Digite a temperatura em graus Celsius: "))

Fahrenheit = Celsius * 1.8 + 32

print(f"A temperatura {Celsius:.2f} Celsius transformada para Celsius e  {Fahrenheit:.2f} Fahrenheit")