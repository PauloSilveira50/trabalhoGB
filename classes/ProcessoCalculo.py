from classes.Processo import Processo

class ProcessoCalculo(Processo):
    def __init__(self, pid:int, tipoProcesso:str, operando1:int, operando2:int, operador:int):
        super().__init__(pid, tipoProcesso) # passamos o pid e o tipoProcesso para a super classe
        self.operando1 = operando1
        self.operando2 = operando2
        self.operador = operador

    def Info(self):
        super().Info()
        print(f'Operador: {self.operador}')
        print(f'Operando1: {self.operando1}')
        print(f'Operando2: {self.operando2}')

    def execute(self):
        match self.operador:
            case 1:
                resposta = self.operando1 + self.operando2
            case 2:
                resposta = self.operando1 - self.operando2
            case 3:
                resposta = self.operando1 * self.operando2
            case 4:
                resposta = self.operando1 / self.operando2

        return resposta