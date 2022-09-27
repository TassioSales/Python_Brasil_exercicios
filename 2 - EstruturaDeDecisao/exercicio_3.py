# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite uma letra F ou M apenas essas: ").upper().strip()[0]

if letra == "M":
    print("Masculino")
elif letra == "F":
    print("Feminino")
else:
    print("Letra invalida")
