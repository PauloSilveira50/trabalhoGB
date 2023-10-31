class ProcessoCalculo(Processo):
    def _init_(self,pid,operando1,operando2,operador):
        super()._init_(pid)
        self.operando1=int(operando1)
        self.operando2=int(operando2)
        self.operador=int(operador)

    def execute(self):
        if self.operador == 1:
            resposta = self.operando1 + self.operando2
        elif self.operador == 2:
            resposta = self.operando1 - self.operando2
        elif self.operador == 3:
            resposta = self.operando1 * self.operando2
        elif self.operador == 4:
            resposta = self.operando1 / self.operando2
        return resposta