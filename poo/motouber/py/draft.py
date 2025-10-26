class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro: int = dinheiro
    def getDinheiro(self):
        return self.__dinheiro
    def setDinheiro(self, valor: int):
        self.__dinheiro += valor
    def getnome(self):
        return self.__nome
    def __str__(self) -> str:
        return f'{self.__nome}:{self.__dinheiro}'
class Moto:
    def __init__(self, motorista: Pessoa, custo: int):
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        self.__custo:int = 0
    
    def __str__(self) -> str:
        driver = str(self.__motorista)
        passg = str(self.__passageiro)
        return f'Cost: {self.__custo}, Driver: {driver}, Passenger: {passg}'
    
    def insertmoto(self, motorista: Pessoa, custo: int):
        self.__motorista = motorista
    def insertpass(self, passageiro: Pessoa, custo: int):
        self.__passageiro = passageiro
    def drive(self, custo: int):
        self.__custo = custo
    def leavepass(self):
        if self.__passageiro == None:
            print('fail: no passenger to leave')
        passageiro = self.__passageiro
        motorista = self.__motorista
        dinheiro_pass = passageiro.getDinheiro()
        custo = self.__custo
        passageiro.setDinheiro(-custo)
        motorista.setDinheiro(custo)
        pessoa_removida = self.__passageiro
        print(f'{pessoa_removida} left')
        self.__passageiro = None
        self.__custo = 0
def main():
    motouber = Moto(None, 0)
    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)
        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(motouber)
        elif args[0] == 'setDriver':
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            motouber.insertmoto(motorista, dinheiro)
        elif args[0] == 'setPass':
            nome = args[1]
            dinheiro = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            motouber.insertpass(passageiro, dinheiro)
        elif args[0] == 'drive':
            custo = int(args[1])
            motouber.drive(custo)
        elif args[0] == 'leavepass':
            motouber.leavepass()
main()