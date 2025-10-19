
class Watch:
    def __init__(self, hora: int = 0, min: int = 0, seg: int = 0):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0
        self.setHora(hora)
        self.setMinuto(min)
        self.setSeg(seg)
    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__min   
    def getSeg(self):
        return self.__seg 


    def setHora(self, valor:int):
        if valor < 0 or valor > 23:
            print('fail: hora invalida')
        else:
            self.__hora = valor
    def setMinuto(self, valor:int):
        if valor < 0 or valor > 59:
            print('fail: minuto invalido')
        else:
            self.__min = valor
    def setSeg(self, valor:int):
        if valor < 0 or valor > 59:
            print('fail: segundo invalido')
        else:
            self.__seg = valor
    def nextSecond(self):
        self.__hora += 1
        if self.__seg >= 59:
            self.__seg = 0
            self.__min = 0
        if self.__hora >= 24:
            self.__hora = 0 
    def __str__(self) -> str:
        return f'{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}'

def main():
        relogio = Watch()
        while True:
            line: str = input()
            args: list[str] = line.split()
            print(f'$' + line)
            if args[0] == 'end':
                break
            elif args[0] == 'show':
                print(relogio)
            elif args[0] == 'init':
                relogio = Watch(int(args[1]), int(args[2]), int(args[3]))
            elif args[0] == 'set':
                relogio.setHora(int(args[1]))
                relogio.setMinuto(int(args[2]))
                relogio.setSeg(int(args[3]))
            elif args[0] == 'next':
                 relogio.nextSecond() 
main()      