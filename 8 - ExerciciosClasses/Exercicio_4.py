"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão,
a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(anos * 0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}'


if __name__ == '__main__':
    pessoa = Pessoa('Joao', 25, 70, 1.70)
    print(pessoa)
    pessoa.envelhecer(1)
    print(pessoa)
    pessoa.engordar(5)
    print(pessoa)
    pessoa.emagrecer(3)
    print(pessoa)
    pessoa.crescer(0.1)
    print(pessoa)