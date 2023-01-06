"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a)"Telefonou para a vítima?"
b)"Esteve no local do crime?"
c)"Mora perto da vítima?"
d)"Devia para a vítima?"
e)"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

#criar função para realizar perguntas

def realizarPerguntas():
    ListaPerguntas = ["Telefonou para a vítima?",
                      "Esteve no local do crime?",
                      "Mora perto da vítima?",
                      "Devia para a vítima?",
                      "Já trabalhou com a vítima?"]
    listaRepostas = []
    for pergunta in ListaPerguntas:
        print(pergunta)
        resposta = input("Qual a resposta para a pergutas ?").upper().strip()[0]
        #aceitas apenas S ou N como resposta:
        if resposta == "S":
            listaRepostas.append(resposta)
        elif resposta == "N":
            listaRepostas.append(resposta)
        else:
            print("Resposta invalida Responda apenas com Sim ou Não")
            while True:
                resposta = input("Qual a resposta para a pergutas ?").upper().strip()[0]
                if resposta == "S":
                    listaRepostas.append(resposta)
                    break
                elif resposta == "N":
                    listaRepostas.append(resposta)
                    break
                else:
                    print("Resposta invalida Responda apenas com Sim ou Não")
        print(listaRepostas)
        
    return listaRepostas

#criar função para classificar a pessoa
def contaResposta(listaRepostas):
    #contar quantos S existem dentro da lista
    contaSim = 0
    for item in listaRepostas:
        if item == "S":
            contaSim += 1
    return contaSim

def classificador(contador):
    if contador == 2:
        print("Essa pessoa possivelmente e uma Suspeita")
    elif contador == 3 or contador == 4:
        print("Essa pessoa possivelmente e uma Cumplice")
    elif contador == 5:
        print("Essa pessoa possivelmente e uma Assassino")
    else:
        print("Essa pessoa possivelmente e uma Inocente")
        
def main():
    perguntas = realizarPerguntas()
    contador = contaResposta(perguntas)
    classificador(contador)
    


if __name__ == '__main__':
    main()
        