"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
        A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
        A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
        A mensagem "Aprovado com Distinção", se a média for igual a 10."""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a Segunda  nota: "))
nota3 = float(input("Digite a Terceira nota: "))

notas =  [nota1, nota2, nota3]

media =  sum(notas) / len(notas)

print(media)