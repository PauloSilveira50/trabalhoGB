class Processo:
    def __init__(self, pid:int, tipoProcesso:str=None):
        self.pid = int(pid)
        self.tipoProcesso = None
        if tipoProcesso != None:
            self.tipoProcesso = str(tipoProcesso)

    def getPid(self):
        return self.pid
    
    def Info(self):
        print(f'PID: {self.pid}')

        if self.tipoProcesso != None:
            print(f'Tipo Processo: {self.tipoProcesso}')

    def execute(self):
        return  