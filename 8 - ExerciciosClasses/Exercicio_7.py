"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,
Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um
atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""


class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def fome(self):
        return self._fome

    @fome.setter
    def fome(self, fome):
        self._fome = fome

    @property
    def saude(self):
        return self._saude

    @saude.setter
    def saude(self, saude):
        self._saude = saude

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def humor(self):
        return self.fome * self.saude

    def __str__(self):
        return f"Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade} Humor: {self.humor()}"

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome


class jogar:
    def __init__(self, bichinho):
        self.bichinho = bichinho

    def menu(self):
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Dormir")
        print("4 - Verificar")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        return opcao

    def alimentar(self):
        self.bichinho.alterar_fome(self.bichinho.fome + 1)
        print("Alimentando...")

    def brincar(self):
        self.bichinho.alterar_saude(self.bichinho.saude + 1)
        print("Brincando...")

    def dormir(self):
        self.bichinho.alterar_fome(self.bichinho.fome - 1)
        self.bichinho.alterar_saude(self.bichinho.saude - 1)
        print("Dormindo...")

    def verificar(self):
        print(self.bichinho)

    def sair(self):
        print("Saindo...")
        exit()

    def opcoes(self, opcao):
        if opcao == 1:
            self.alimentar()
        elif opcao == 2:
            self.brincar()
        elif opcao == 3:
            self.dormir()
        elif opcao == 4:
            self.verificar()
        elif opcao == 5:
            self.sair()
        else:
            print("Opção inválida!")

    def iniciar(self):
        while True:
            opcao = self.menu()
            self.opcoes(opcao)


if __name__ == '__main__':
    try:
        nome = input("Digite o nome do bichinho: ")
        fome = int(input("Digite a fome do bichinho: "))
        saude = int(input("Digite a saúde do bichinho: "))
        idade = int(input("Digite a idade do bichinho: "))
        bichinho = BichinhoVirtual(nome, fome, saude, idade)
        jogo = jogar(bichinho)
        jogo.iniciar()
    except ValueError:
        print("Valor inválido!")

