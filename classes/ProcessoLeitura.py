import csv
import re
from classes.Processo import Processo
from classes.Sistema import *
from classes.ProcessoCalculo import *
from classes.ProcessoGravacao import *
from colorama import Fore

class ProcessoLeitura(Processo):
    #Passamos o pid e o arquivo com as expressões
    def __init__(self,pid,arquivo):
        super().__init__(pid)
        self.pid=int(pid)
        self.arquivo=arquivo

    def getPid(self):
        return self.pid

    def execute(self):
        #Transforma o arquivo de texto em uma tabela
        pou = open(self.arquivo)
        rComputation = csv.reader(pou)
        calculos = list(rComputation)
        linhas=len(calculos)
        self.pid += 1
        #Separamos cada elemento das expresões por linhas da tabela
        for l in range(linhas):
            expressao = (calculos[l][0])
            operando1 = re.findall(r'\d+',expressao)[0]
            operando2 = re.findall(r'\d+',expressao)[2]
            operador = re.findall(r'[+\-*/]', expressao)[0]
            if operador == '+':
                operador = 1
            elif operador == '-':
                operador = 2
            elif operador == '*':
                operador = 3
            else:
                operador = 4
            #Chamamos o processo cálculo para execução
            processo = Processo(self.pid, 'Cálculo')
            processoCalculo = ProcessoCalculo(self.pid, processo.getTipoProcesso(), float(operando1), float(operando2), operador)
            listaProcessos.append([self.pid, str(processo.getTipoProcesso())])
            listaProcessosCalculo.append([self.pid, processoCalculo.operando1, processoCalculo.operador, processoCalculo.operando2])
            #Aumentamos em 1 o id de processo 
            self.pid += 1
        open(self.arquivo, 'w')
        