from classes.Processo import *
from classes.ProcessoCalculo import *
from classes.ProcessoEscrita import *
from classes.ProcessoGravacao import *
from classes.ProcessoLeitura import *

if __name__ == "__main__":
    processo1 = Processo(1)

    processo1.Info()

    processoCalculo1 = ProcessoCalculo(processo1.getPid(), 'Calculo', 1, 1, 1)