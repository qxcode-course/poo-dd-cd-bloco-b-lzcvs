class Camisa:
    def __init__(self):
        self.__tamanho: str = ''
    def getTamanho(self) -> str:
        return self.__tamanho
    def setTamanho(self, valor: str) -> str:
        if valor == 'PP' or valor == 'P' or valor == 'M' or valor == 'G' or valor == 'GG' or valor == 'XG':
            return self.__tamanho
        else:
            return 'fail: Valor Invalido, tente PP, P M, G, GG ou XG'
    
def main():
    camisa = Camisa()
    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(f'size: ({camisa.getTamanho()})')
        else:
            ('comando invalido')
main()