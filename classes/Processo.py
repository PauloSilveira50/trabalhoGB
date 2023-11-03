class Processo:
    def __init__(self, pid: int, tipoProcesso: str = None):
        self.pid = pid
        self.tipoProcesso = tipoProcesso

    def getPid(self):
        return self.pid
    
    def Info(self):
        print(f'PID: {self.pid}')

        if self.tipoProcesso != None:
            print(f'Tipo Processo: {self.tipoProcesso}')

    def execute(self):
        return  