"""Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de
comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão
rapidamente os níveis de fome e tédio caem.

Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do
#objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
#Dica: acrescente um método especial str() à classe Bichinho.

Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho,
exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para
todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

"""


class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade}'

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude

    def setIdade(self, idade):
        self.idade = idade

    def alimentar(self, comida):
        self.fome -= comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.saude += tempo
        if self.saude > 100:
            self.saude = 100

    def envelhecer(self, anos):
        self.idade += anos
        self.fome += anos * 10
        self.saude -= anos * 5
        if self.fome > 100:
            self.fome = 100
        if self.saude < 0:
            self.saude = 0

    def status(self):
        print(f'Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade}')


if __name__ == '__main__':
    bichinho = BichinhoVirtual('Bichinho', 50, 50, 1)


    def menu():
        print('1 - Alimentar')
        print('2 - Brincar')
        print('3 - Envelhecer')
        print('4 - Status')
        print('5 - Sair')
        return int(input('Escolha uma opção: '))


    while True:
        opcao = menu()
        if opcao == 1:
            comida = int(input('Quantos gramas de comida? '))
            bichinho.alimentar(comida)

        elif opcao == 2:
            tempo = int(input('Quantos minutos de brincadeira? '))
            bichinho.brincar(tempo)

        elif opcao == 3:
            anos = int(input('Quantos anos? '))
            bichinho.envelhecer(anos)

        elif opcao == 4:
            bichinho.status()

        elif opcao == 5:
            break

