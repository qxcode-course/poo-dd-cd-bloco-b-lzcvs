class Chinelo:
    def __init__(self):
        self.__tamanho = 0
    def getTamnho(self):
        return self.__tamanho
    def setTamanho(self, num:int):
        if num >= 20 and num <= 50 and num % 2 == 0:
            self.__tamanho = num
            print(f'{self.__tamanho} escolhido com sucesso')
        else:
            print(f'nao vai ta tendo desse...')

chinela = Chinelo()

while chinela.getTamnho() == 0:
    tamanho = int(input('digite um número: '))
    chinela.setTamanho(tamanho)