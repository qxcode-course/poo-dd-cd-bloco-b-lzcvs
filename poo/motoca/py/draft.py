class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getage(self):
        return self.__age
    def getnome(self):
        return self.__name
    def __str__(self) -> str:
        return f'{self.__name}:{self.__age}'

class Moto:
    def __init__(self, potencia: int):
        self.__potencia = potencia
        self.__time: int = 0
        self.__pessoa: Pessoa | None = None
    
    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print('fail: busy motorcycle')
            return False
        self.__pessoa = pessoa
        return True

    def __str__(self) -> str:
        if self.__pessoa is None:
            nome = 'empty'
            return f'power:{self.__potencia}, time:{self.__time}, person:({nome})'
        return f'power:{self.__potencia}, time:{self.__time}, person:({self.__pessoa})'
    
    def remover(self) -> Pessoa | None:
        if self.__pessoa is None:
            print('fail: empty motorcycle')
            return None
        pessoa_removida = self.__pessoa
        self.__pessoa = None
        print(pessoa_removida)
    def buytime(self, time: int):
        self.__time += time
def main():
    moto = Moto(1)

    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            potencia = args[1]
            moto = Moto(potencia)     
        elif args[0] == 'show':
            print(moto)
        elif args[0] == 'enter':
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            moto.inserir(pessoa)
        elif args[0] == 'leave':
            moto.remover()
        elif args[0] == 'buy':
            tempo = int(args[1])
            moto.buytime(tempo)
main()