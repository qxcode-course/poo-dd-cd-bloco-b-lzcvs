class Camisa:
    def __init__(self):
        self.__tamanho: str = ''
    def getTamanho(self) -> str:
        return self.__tamanho
    def setTamanho(self, valor: str) -> str:
        if valor == 'PP' or valor == 'P' or valor == 'M' or valor == 'G' or valor == 'GG' or valor == 'XG':
            self.__tamanho = valor
            return valor
        else:
            print('fail: Valor inválido, tente PP, P, M, G, GG ou XG')
    def show(self) -> None:
        print(f"size: ({self.__tamanho})")
def main():
    camisa = Camisa()
    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            camisa.show()
        elif args[0] == 'size':
            valor = args[1]
            camisa.setTamanho(valor)
        else:
            ('comando invalido')
main()