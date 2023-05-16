"""Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno
programa que teste sua classe.

Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem."""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f'Nome: {self.nome} Salário: R${self.salario:.2f}'

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def setNome(self, nome):
        self.nome = nome

    def setSalario(self, salario):
        self.salario = salario

    def aumentaSalario(self, percentual):
        self.salario += self.salario * percentual

    def reduzSalario(self, percentual):
        self.salario -= self.salario * percentual


if __name__ == '__main__':
    funcionario = Funcionario('João', 1000)
    print(funcionario)
    funcionario.aumentaSalario(0.2)
    print(funcionario)
    funcionario.reduzSalario(0.1)
    print(funcionario)
