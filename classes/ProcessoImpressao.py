from classes.Processo import Processo
from classes.Sistema import *
from classes.ProcessoCalculo import *
from classes.ProcessoGravacao import *
from colorama import Fore

class ProcessoImpressao(Processo):
    def __init__(self, pid: int):
        super().__init__(pid)

    def execute(self):
        print('-'*50)
        i = 0
        c = 0
        g = 0
        for p in listaProcessos:
            i += 1
            if p[1] == 'Cálculo':
                if listaProcessosCalculo[c][2] == 1.0:
                    print(f'{i} | PID: {p[0]} | Tipo Processo: {Fore.YELLOW + p[1] + Fore.WHITE} | Operador 1: {listaProcessosCalculo[c][1]} | Operando: Soma | Operador 2: {listaProcessosCalculo[c][3]}')

                if listaProcessosCalculo[c][2] == 2.0:
                    print(f'{i} | PID: {p[0]} | Tipo Processo: {Fore.YELLOW + p[1] + Fore.WHITE} | Operador 1: {listaProcessosCalculo[c][1]} | Operando: Subtração | Operador 2: {listaProcessosCalculo[c][3]}')
                
                if listaProcessosCalculo[c][2] == 3.0:
                    print(f'{i} | PID: {p[0]} | Tipo Processo: {Fore.YELLOW + p[1] + Fore.WHITE} | Operador 1: {listaProcessosCalculo[c][1]} | Operando: Multiplicação | Operador 2: {listaProcessosCalculo[c][3]}')
                
                if listaProcessosCalculo[c][2] == 4.0:
                    print(f'{i} | PID: {p[0]} | Tipo Processo: {Fore.YELLOW + p[1] + Fore.WHITE} | Operador 1: {listaProcessosCalculo[c][1]} | Operando: Divisão | Operador 2: {listaProcessosCalculo[c][3]}')
                c += 1
            elif p[1] == 'Gravação':
                print(f'{i} | PID: {p[0]} | Tipo Processo: {p[1]} | Expressão: {listaProcessosGravacao[g][2]}')
                g += 1
                #print(f'{i} | PID: {p[0]} | Tipo Processo: {p[1]} | ')
            else:
                print(f'{i} | PID: {p[0]} | Tipo Processo: {p[1]}')