"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos"""


#função para gerar uma lista com 30 alunos com idades e alturas aleatorias sendo a idade entre 10 e 20 e a altura entre 1.4 e 2.0 arredondada para duas casas decimais 

def gerarListaAlunos():
    import random
    listaAlunos = []
    for i in range(30):
        idade = random.randint(10,20)
        altura = round(random.uniform(1.4,2.0),2)
        listaAlunos.append([idade,altura])
    return listaAlunos

#função para calcular a media de altura dos alunos
def mediaAltura(listaAlunos):
    soma = 0
    for item in listaAlunos:
        soma += item[1]
    return soma/len(listaAlunos)

#função para contar a quantidade de alunos com mais de 13 anos e altura inferior a media de altura
def alunosComMaisDe13Anos(listaAlunos):
    contador = 0
    media = mediaAltura(listaAlunos)
    for item in listaAlunos:
        if item[0] > 13 and item[1] < media:
            contador += 1
    return contador

def main():
    listaAlunos = gerarListaAlunos()
    print(f"Lista de alunos: {listaAlunos}")
    print(f"Quantidade de alunos com mais de 13 anos e altura inferior a media de altura: {alunosComMaisDe13Anos(listaAlunos)}")
    
if __name__ == '__main__':
    main()