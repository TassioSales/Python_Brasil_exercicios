"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

class Meta:
    def __init__(self):
        self.identificacao = 0
        self.defeito = 0
        self.lista = []
        self.esfera = 0
        self.limpeza = 0
        self.cabo = 0
        self.quebrado = 0
    
    def menu(self):
        print('''
        1- necessita da esfera
        2- necessita de limpeza
        3- necessita troca do cabo ou conector
        4- quebrado ou inutilizado
        0- Sair
        ''')

    def calcula(self):
        while True:
            self.identificacao = int(input('Digite a identificação do mouse: '))
            if self.identificacao == 0:
                break
            else:
                self.menu()
                self.defeito = int(input('Digite o defeito: '))
                if self.defeito == 0:
                    break
                elif self.defeito > 4:
                    print('Opção inválida!')
                else:
                    self.lista.append(self.defeito)
        self.esfera = self.lista.count(1)
        self.limpeza = self.lista.count(2)
        self.cabo = self.lista.count(3)
        self.quebrado = self.lista.count(4)
        print(f'''
        Quantidade de mouses: {len(self.lista)}
        
        Situação                        Quantidade              Percentual
        1- necessita da esfera                  {self.esfera}                     {self.esfera / len(self.lista) * 100}%
        2- necessita de limpeza                 {self.limpeza}                     {self.limpeza / len(self.lista) * 100}%
        3- necessita troca do cabo ou conector  {self.cabo}                     {self.cabo / len(self.lista) * 100}%
        4- quebrado ou inutilizado              {self.quebrado}                     {self.quebrado / len(self.lista) * 100}%
        ''')
        

if __name__ == '__main__':
    meta = Meta()
    meta.calcula()