class Grafite:
    def __init__(self, thickness: float, hardness: str, size:int):
        self.__size = size
        self.__thickness = thickness
        self.__hardness = hardness

    def getthickness(self):
        return self.__thickness
    def gethardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    def thickness(self):
        return self.__thickness
    def __str__(self):
        return f'[{self.__thickness}:{self.__hardness}:{self.__size}]'
class Lapiseira:
    def __init__(self, calibre):
        self.__calibre = calibre
        self.__grafite = None

    def temGrafite(self) -> bool:
        return self.__grafite is not None

    def inserir(self, grafite: Grafite) -> bool:
        if grafite.getthickness() != self.__calibre:
            print('fail: calibre incompativel')
            return False
        if self.__grafite is not None:
            print('fail: ja existe grafite')
            return False
        self.__grafite = grafite
        return True
    def remover(self) -> Grafite | None:
        grafite_removido = self.__grafite
        self.__grafite = None
    def escrever(self):
        if self.__grafite == None:
            print('fail: nao existe grafite')
            return self.__grafite
        
    def __str__(self) -> str:
        if self.__grafite == None:
            estado = 'null'
            return f'calibre: {self.__calibre}, grafite: {estado}'
        return f'calibre: {self.__calibre}, grafite: {self.__grafite}'

def main():
    polis = Lapiseira(' ')
    while True: 
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)

        if args[0] == 'end': 
            break
        elif args[0] == 'init':
            calibre = float(args[1])
            polis = Lapiseira(calibre)
        elif args[0] == 'show':
            print(polis)
        elif args[0] == 'insert':
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            graf = Grafite(thickness, hardness, size)
            polis.inserir(graf)
        elif args[0] == 'remove':
            polis.remover()
        elif args[0] == 'write':
            polis.escrever()
main()