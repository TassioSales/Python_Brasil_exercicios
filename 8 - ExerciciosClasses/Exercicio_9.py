"""Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y. Possua uma classe chamada Retangulo, com os atributos
largura e altura. Possua uma função para imprimir os valores da classe Ponto Possua uma função para encontrar o
centro de um Retângulo. Você deve criar alguns objetos da classe Retangulo. Cada objeto deve ter um vértice de
partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto. A função para
encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y
para o centro do objeto. O valor do centro do objeto deve ser mostrado na tela Crie um menu para alterar os valores
do retângulo e imprimir o centro deste retângulo."""


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Retangulo:
    def __init__(self, largura, altura, vertice):
        self.largura = largura
        self.altura = altura
        self.vertice = vertice

    def centro(self):
        x = self.vertice.x + self.largura / 2
        y = self.vertice.y + self.altura / 2
        return Ponto(x, y)

    def __str__(self):
        return f'({self.vertice.x}, {self.vertice.y}), {self.largura}, {self.altura}'


def main():
    vertice = Ponto(10, 10)
    retangulo = Retangulo(10, 10, vertice)
    print(f'Vertice: {retangulo.vertice}')
    print(f'Centro: {retangulo.centro()}')
    print(f'Retangulo: {retangulo}')


if __name__ == '__main__':
    main()