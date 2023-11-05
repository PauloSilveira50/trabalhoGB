import csv
from classes.ProcessoCalculo import *
from classes.Processo import Processo
class ProcessoGravacao(Processo):
    def __init__(self, pid: int, processoCalculo: ProcessoCalculo):
        super().__init__(pid)
        self.processoCalculo = processoCalculo

    def execute(self):
        # Pega todos os dados do arquivo csv
        f = open('trabalhoGB/computation.csv')
        reader = csv.reader(f)
        data = list(reader)
        f.close()

        # Salva linha por linha da matriz, deixando a expressão do processo novo por ultimo
        f = open('trabalhoGB/computation.csv', 'w')
        writer = csv.writer(f)
        for linha in data:
           writer.writerow(l[0], l[1])
        writer.writerow(super().getPid() , self.processoCalculo.expressao())
        f.close()