class Camisa:
    def __init__(self):
        self.__tamanho: str = ''
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, valor: str) -> str:
        if valor == 'PP' or valor == 'P' or valor == 'M' or valor == 'G' or valor == 'XG' or valor == 'GG':
            self.__tamanho = valor
            print(f'{self.__tamanho} escolhido com sucesso')
        else:
            print('tamanho invalido')

camisa = Camisa()

while camisa.getTamanho() == '':
    print("Digite seu tamanho de roupa")
    tamanho = input()
    camisa.setTamanho(tamanho) 