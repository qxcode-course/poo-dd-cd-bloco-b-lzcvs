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
        self.__custo += custo
        return self.__custo
    def leavepass(self):
        passageiro = self.__passageiro
        motorista = self.__motorista
        custo = self.__custo
        dinheiro_pass = passageiro.getDinheiro()
        if self.__passageiro == None:
            print('fail: no passenger to leave')
        if self.__passageiro.getDinheiro() < custo:
            print('fail: Passenger does not have enough money')
        if dinheiro_pass >= custo:
            passageiro.setDinheiro(-custo)
            motorista.setDinheiro(custo)
        else:
            valor_pagar = dinheiro_pass
            passageiro.setDinheiro(-valor_pagar)
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
        elif args[0] == 'leavePass':
            motouber.leavepass()
main()