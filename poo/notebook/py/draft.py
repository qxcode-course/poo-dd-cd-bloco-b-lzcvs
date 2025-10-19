class Notebook:
    # ligar desligar
    # mostrar
    # usar
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None

    def mostrarLigado(self):
        print(self.__bateria)
        print(self.__ligado)
    def set_bateria(self):
        self.__bateria = bateria
    def get_bateria(self):
        return self.__bateria
    def mostrar(self):
        if self.__ligado == False and self.__bateria == None:
            print('msg: notebook desligado e sem bateria')
        elif self.__ligado == True and self.__bateria == None:
            print('msg: notebook sem bateria')
        else:
            print('msg: notebook ligado')

    def setLigado(self, valor):
        if isinstance(valor, bool):
            self.__ligado = valor

    def usar(self, valor: int):
        if self.__ligado == False:
            print('msg: erro: ligue o notebook primeiro')
        if self.__bateria == None:
            print('msg: sem bateria')
        else:
            print(f'msg: usando por {valor} minutos')

    def ligar(self):
        if self.__ligado == False:
            self.__ligado = True
            print('msg: notebook ligado')
        if self.__bateria == None:
            print('msg: sem bateria')

    def desligar(self):
        if self.__ligado == True:
            self.__ligado = False
            print('msg: notebook desligado')

class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade   

    def getcarga(self):
        return self.__carga
        
    def getcapacidade(self):
        return self.__capacidade
    def setcapacidade(self, valor:int):
        if valor > 0:
            self.__capacidade = valor

    def setcarga(self, valor:int):
        if valor > 0:
            self.__carga = valor

    def __str__(self):
        return f"Bateria({self.__carga}/{self.__capacidade})"

notebook = Notebook()
notebook.mostrar()
notebook.usar(20)
notebook.ligar()
notebook.usar(20)
notebook.mostrarLigado()
notebook.desligar()
notebook.mostrarLigado()
notebook.usar(20)
bateria = Bateria(20)
