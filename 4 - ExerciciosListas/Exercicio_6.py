"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

#função para pedir a media de 10 alunos
def mediaAlunos():
    listaMedia = []
    for i in range(10):
        media = float(input(f"Digite a media do aluno {i+1}: "))
        listaMedia.append(media)
    return listaMedia

#função para contar a quantidade de alunos com media maior ou igual a 7
def mediaMaiorQueSete(listaMedia):
    contador = 0
    for item in listaMedia:
        if item >= 7:
            contador += 1
    return contador

def main():
    listaMedia = mediaAlunos()
    print(f"Lista de medias: {listaMedia}")
    print(f"Quantidade de alunos com media maior ou igual a 7: {mediaMaiorQueSete(listaMedia)}")
    
if __name__ == '__main__':
    main()