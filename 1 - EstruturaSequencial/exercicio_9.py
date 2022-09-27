#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

Fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celcius = 5 * ((Fahrenheit - 32) / 9)

print(f"A temperatura {Fahrenheit} Fahrenheit transformada para Celsius e {celcius:.2f} Celsius")