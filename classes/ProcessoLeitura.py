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

    def leitura(self):
        #Transforma o arquivo de texto em uma tabela
        pou = open(self.arquivo)
        rComputation = csv.reader(pou)
        calculos = list(rComputation)
        linhas=len(calculos)
        #Separamos cada elemento das expresões por linhas da tabela
        for l in range(linhas):
            operando1 = calculos[l][0]
            operando2 = calculos[l][2]
            operador = calculos[l][1]
        print('-'*50)
        #Chamamos o processo cálculo para execução
        processo = Processo(self.pid, 'Cálculo')
        processoCalculo = ProcessoCalculo(processo.getPid(), processo.getTipoProcesso(), operando1, operando2, operador)
        listaProcessos.append([processo.getPid(), str(processo.getTipoProcesso())])
        listaProcessosCalculo.append([processo.getPid(), processoCalculo.operando1, processoCalculo.operador, processoCalculo.operando2])
        #Aumentamos em 1 o id de processo 
        self.pid += 1
        print('Processo do TIPO CÁLCULO' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE) # Imprime o texto em verde