"""Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada
com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na
tela, informando se o usuário ganhou ou perdeu o jogo."""

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


# função para embaralhar a palavra

def embaralharPalavra(palavra):
    try:
        palavra = list(palavra)
        random.shuffle(palavra)
        palavra = ''.join(palavra)
        return palavra
    except Exception as e:
        print(e)
        return embaralharPalavra(palavra)

# função para remover acentos e caracteres especiais da palavra

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


# função para jogar o jogo

def jogar():
    try:
        palavra = getPalavra()
        palavra = removerCaracteresEspeciais(palavra)
        palavraEmbaralhada = embaralharPalavra(palavra)
        print(f'A palavra é: {palavraEmbaralhada}')
        tentativas = 6
        while tentativas > 0:
            letra = input('Digite uma letra: ')
            if letra in palavra:
                print(f'A palavra é: {palavraEmbaralhada}')
            else:
                tentativas -= 1
                print(f'-> Você errou pela {6 - tentativas}ª vez. Tente de novo!')
        print(f'A palavra é: {palavra}')
    except Exception as e:
        print(e)
        return jogar()


if __name__ == '__main__':
    jogar()
