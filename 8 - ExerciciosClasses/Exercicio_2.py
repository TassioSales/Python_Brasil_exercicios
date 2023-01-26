"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    @property
    def tamanho_lado(self):
        return self._tamanho_lado

    @tamanho_lado.setter
    def tamanho_lado(self, tamanho_lado):
        self._tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado


if __name__ == '__main__':
    quadrado = Quadrado(10)
    print(f'O tamanho do lado é {quadrado.retornar_valor_lado()} e a área é {quadrado.calcular_area()}')
    quadrado.mudar_valor_lado(20)
    print(f'O tamanho do lado é {quadrado.retornar_valor_lado()} e a área é {quadrado.calcular_area()}')
