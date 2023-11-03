from colorama import init, Fore
from time import sleep
from classes.Processo import *
from classes.ProcessoCalculo import *
from classes.ProcessoEscrita import *
from classes.ProcessoGravacao import *
from classes.ProcessoLeitura import *
from classes.Sistema import *

if __name__ == "__main__":
    i = 0
    while True: # Cria um Loop Para o Menu Principal
        MenuPrincipal.mainMenu() # Impressão do Menu Principal
        sleep(1)
        print('-'*50)
        escolhaPrincipal = int(input('Qual a sua escolha? '))
        
        if escolhaPrincipal not in (1, 2, 3, 4, 5, 0): # Se a escolha não for válida
            sleep(1) 
            print('-'*50)
            print(Fore.RED + 'Opção escolhida não é válida. Tente novamente!' + Fore.WHITE) # Imprime o texto em vermelho
            sleep(1)

        match escolhaPrincipal:

            case 1: # Criar Processo
                sleep(1)
                MenuPrincipal.opcoesProcessos()
                escolhaTipoProcesso = int(input('Escolha do Tipo de Processo: '))
                match escolhaTipoProcesso:
                    case 1: # cálculo
                        sleep(1)
                        print('-'*50)
                        operando1 = float(input('Digite o primeiro número (Operando1): '))
                        sleep(1)
                        MenuPrincipal.opcoesOperador()
                        operador = float(input('Escolha o Operador do cálculo: '))
                        sleep(1)
                        print('-'*50)
                        operando2 = float(input('Digite o segundo número (Operando2): '))
                        print('-'*50)
                        i += 1
                        processo = Processo(i, 'Cálculo')
                        processoCalculo = ProcessoCalculo(processo.getPid(), processo.getTipoProcesso(), operando1, operando2, operador)
                        listaProcessos.append([str(processo.getPid()), str(processo.getTipoProcesso())])
                        sleep(1)
                        print('Processo do TIPO CÁLCULO' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE) # Imprime o texto em verde
                    case 2: # gravação
                        pass
                    case 3: # leitura
                        pass
                    case 4: # impressão
                        pass

            case 2: # Executar Próximo Processo
                sleep(1)
                pass
            
            case 3: # Executar Processo Específico
                sleep(1)
                pass
            
            case 4: # Salvar a Fila de Processos
                sleep(1)
                pass
            
            case 5: # Carregar do Arquivo a Fila de Processos
                sleep(1)
                pass
            
            case 0: # Sair do Sistema
                print('-'*50)
                num = 0
                for l in listaProcessos:
                    num += 1
                    print(f'{num} | PID: {l[0]} | Tipo Processo: {l[1]}')
                #sleep(1)
                #MenuPrincipal.desligandoSistema() # Imprime Mensagens de Desligamento Dinâmicas
                #break # Quebra o Loop do Menu Principal