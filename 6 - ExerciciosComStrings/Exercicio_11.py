"""Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!"""

import random
import re


# função para ler o arquivo de palavras.txt

def lerArquivo():
    try:
        with open('palavras.txt', 'r') as arquivo:
            palavras = arquivo.read()
            palavras = palavras.split()
            return palavras
    except Exception as e:
        print(e)
        return lerArquivo()


# função para criar uma lista de palavras do arquivo

def getPalavra():
    try:
        palavras = lerArquivo()
        palavra = random.choice(palavras)
        return palavra
    except Exception as e:
        print(e)
        return getPalavra()


# remover acentos e caracteres especiais da palavra

def removerCaracteresEspeciais(palavra):
    try:
        palavra = palavra.lower()
        palavra = re.sub('[^a-zA-Z0-9 \\\]', '', palavra)
        # remover acentos usando o regex
        palavra = re.sub('[áàâã]', 'a', palavra)
        palavra = re.sub('[éèê]', 'e', palavra)
        palavra = re.sub('[íìî]', 'i', palavra)
        palavra = re.sub('[óòôõ]', 'o', palavra)
        palavra = re.sub('[úùû]', 'u', palavra)
        palavra = re.sub('[ç]', 'c', palavra)
        return palavra
    except Exception as e:
        print(e)
        return removerCaracteresEspeciais(palavra)


# função para pedir letra ao usuário e verificar se a letra está na palavra

def pedirLetra(palavra):
    try:
        palavra = removerCaracteresEspeciais(palavra)
        letras = []
        for i in range(len(palavra)):
            letras.append('_')
        print(letras)
        while True:
            # pedir letra ao usuário e verificar se a letra está na palavra e mostrar a letra na posição correta
            letra = input('Digite uma letra: ')
            letra = removerCaracteresEspeciais(letra)
            if letra in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        letras[i] = letra
                print(letras)
                if '_' not in letras:
                    print('Você ganhou!')
                    break
            else:
                print('A letra não está na palavra')
    except Exception as e:
        print(e)
        return pedirLetra(palavra)


# função para  limiter o número de tentativas apartir do número de letras da palavra

def limitarTentativas(palavra):
    try:
        palavra = removerCaracteresEspeciais(palavra)
        return len(palavra) + 1
    except Exception as e:
        print(e)
        return limitarTentativas(palavra)


# função para criar pontos de acordo com o número de letras da palavra

def criarPontos(palavra):
    try:
        palavra = removerCaracteresEspeciais(palavra)
        return len(palavra) * 10
    except Exception as e:
        print(e)
        return criarPontos(palavra)


def mostraResultado(palavra):
    try:
        palavra = removerCaracteresEspeciais(palavra)
        print(f'A palavra era: {palavra}')
    except Exception as e:
        print(e)
        return mostraResultado(palavra)


def main():
    try:
        palavra = getPalavra()
        print(palavra)
        pedirLetra(palavra)
        mostraResultado(palavra)
    except Exception as e:
        print(e)
        return main()


if __name__ == '__main__':
    main()
