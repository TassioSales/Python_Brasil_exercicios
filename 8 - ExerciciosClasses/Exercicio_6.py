"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class TV:
    def __init__(self, canal=2, volume=5):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, canal):
        if 1 <= canal <= 99:
            self._canal = canal
        else:
            print('Canal inválido')

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if 0 <= volume <= 100:
            self._volume = volume
        else:
            print('Volume inválido')

    def alterar_canal(self, canal):
        self.canal = canal

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def __str__(self):
        return f'Canal: {self.canal}\nVolume: {self.volume}'
    
if __name__ == '__main__':
    tv = TV()
    print(tv)
    tv.alterar_canal(30)
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.diminuir_volume()
    print(tv)