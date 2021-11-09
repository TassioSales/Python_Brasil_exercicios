# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite um letra: ")
vogais = "aAeEiIoOuU"

if letra in vogais:
    print(f"Vogal {letra}")
else:
    print(f"Consoante {letra}")
