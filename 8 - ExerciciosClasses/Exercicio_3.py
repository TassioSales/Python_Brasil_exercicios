"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher) Métodos: Mudar valor dos lados,
Retornar valor dos lados, calcular Área e calcular Perímetro; Crie um programa que utilize esta classe. Ele deve
pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a
quantidade de pisos e de rodapés necessárias para o local."""

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    @property
    def lado_a(self):
        return self._lado_a

    @lado_a.setter
    def lado_a(self, lado_a):
        self._lado_a = lado_a

    @property
    def lado_b(self):
        return self._lado_b

    @lado_b.setter
    def lado_b(self, lado_b):
        self._lado_b = lado_b

    def mudar_valor_lados(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def retornar_valor_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


if __name__ == '__main__':
    lado_a = int(input('Digite o valor do lado A: '))
    lado_b = int(input('Digite o valor do lado B: '))
    retangulo = Retangulo(lado_a, lado_b)
    print(f'O valor dos lados é {retangulo.retornar_valor_lados()} e a área é {retangulo.calcular_area()} '
          f'e o perímetro é {retangulo.calcular_perimetro()}')
    lado_a = int(input('Digite o valor do lado A: '))
    lado_b = int(input('Digite o valor do lado B: '))
    retangulo.mudar_valor_lados(lado_a, lado_b)
    print(f'O valor dos lados é {retangulo.retornar_valor_lados()} e a área é {retangulo.calcular_area()} '
          f'e o perímetro é {retangulo.calcular_perimetro()}')