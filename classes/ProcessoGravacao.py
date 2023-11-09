import csv
from classes.ProcessoCalculo import *
from classes.Processo import Processo
class ProcessoGravacao(Processo):
    def __init__(self, pid: int, processoCalculo: ProcessoCalculo):
        super().__init__(pid)
        self.processoCalculo = processoCalculo

    def execute(self):
        # Salva linha por linha da matriz, deixando a expressão do processo novo por ultimo
        f = open('trabalhoGB/computation.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([self.processoCalculo])
