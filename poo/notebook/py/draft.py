class Notebook:
    # ligar desligar
    # mostrar
    # usar
    def __init__(self):
        self.__ligado: bool = False
    def mostrar(self):
        if self.__ligado == False:
            print('msg: notebook desligado')
        else:
            print('msg: notebook ligado')
    def mostrarLigado(self):
        print(self.__ligado)
    def setLigado(self, valor):
        if isinstance(valor, bool):
            self.__ligado = valor
    def usar(self, valor: int):
        if self.__ligado == False:
            print('msg: erro: ligue o notebook primeiro')
        else:
            print(f'msg: usando por {valor} minutos')
    def ligar(self):
        if self.__ligado == False:
            self.__ligado = True
            print('msg: notebook ligado')
    def desligar(self):
        if self.__ligado == True:
            self.__ligado = False
            print('msg: notebook desligado')
        
notebook = Notebook()
notebook.mostrar()
notebook.usar(20)
notebook.ligar()
notebook.usar(20)
notebook.mostrarLigado()
notebook.desligar()
notebook.mostrarLigado()
notebook.usar(20)