import os
from colorama import init, Fore
from time import sleep
from classes.Processo import *
from classes.ProcessoCalculo import *
from classes.ProcessoImpressao import *
from classes.ProcessoGravacao import *
from classes.ProcessoLeitura import *
from classes.Sistema import *

if __name__ == "__main__":
    os.system('cls') or None
    i = 0
    while True: # Cria um Loop Para o Menu Principal
        MenuPrincipal.mainMenu() # Impressão do Menu Principal
        print('-'*50)
        escolhaPrincipal = int(input('Qual a sua escolha? '))
        
        if escolhaPrincipal not in (1, 2, 3, 4, 5, 6, 0): # Se a escolha não for válida
            print('-'*50)
            print(Fore.RED + 'Opção escolhida não é válida. Tente novamente!' + Fore.WHITE) # Imprime o texto em vermelho

        match escolhaPrincipal:
            case 1: # Criar Processo
                MenuPrincipal.opcoesProcessos()
                escolhaTipoProcesso = int(input('Escolha do Tipo de Processo: '))
                
                match escolhaTipoProcesso:
                    case 1: # cálculo
                        print('-'*50)
                        operando1 = float(input('Digite o primeiro número (Operando1): '))
                        MenuPrincipal.opcoesOperador()
                        operador = float(input('Escolha o Operador do cálculo: '))                        
                        print('-'*50)
                        operando2 = float(input('Digite o segundo número (Operando2): '))
                        print('-'*50)
                        i += 1
                        processo = Processo(i, 'Cálculo')
                        processoCalculo = ProcessoCalculo(processo.getPid(), processo.getTipoProcesso(), operando1, operando2, operador)
                        listaProcessos.append([processo.getPid(), str(processo.getTipoProcesso())])
                        listaProcessosCalculo.append([processo.getPid(), processoCalculo.operando1, processoCalculo.operador, processoCalculo.operando2])
                        print('Processo do TIPO CÁLCULO' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE) # Imprime o texto em verde
                    
                    case 2: # gravação
                        print('-'*50) 
                        num = 0
                        if len(listaProcessos) == 0:
                            print(Fore.RED + 'Tente criar um processo do tipo CÁLCULO antes!' + Fore.WHITE) 
                        else:
                            for l in listaProcessos:
                                if l[1] == 'Cálculo':
                                    num += 1
                                    print(f'{num} | PID: {l[0]} | Tipo Processo: {l[1]}')
                            print('-'*50)
                            escolhaProcesso = int(input('Informe o PID do Processo que deseja gravar? '))
                            print('-'*50)
                            if l[0] == escolhaProcesso:
                                for c in listaProcessosCalculo:
                                    if l[0] == c[0]:
                                        processoCalculo = ProcessoCalculo(l[0], l[1], c[1], c[3], c[2])
                                        i += 1
                                        processo = Processo(i, 'Gravação')
                                        processoGravacao = ProcessoGravacao(i, processoCalculo.expressao())
                                        listaProcessos.append([processo.getPid(), str(processo.getTipoProcesso())])
                                        listaProcessosGravacao.append([processo.getPid(), str(processo.getTipoProcesso()), str(processoCalculo.expressao())])
                                        print('Processo do TIPO GRAVAÇÃO' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE)

                            elif (l == listaProcessos[-1]) and (num == 0):
                                print(Fore.RED + 'Tente criar um processo do tipo CÁLCULO antes!' + Fore.WHITE)       
                    
                    case 3: # leitura
                        print('-'*50)
                        i += 1
                        processo = Processo(i, 'Leitura')
                        listaProcessos.append([processo.getPid(), str(processo.getTipoProcesso())])
                        print('Processo do TIPO LEITURA' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE)
                    
                    case 4: # impressão
                        print('-'*50)
                        i += 1
                        processo = Processo(i, 'Impressão')
                        listaProcessos.append([processo.getPid(), str(processo.getTipoProcesso())])
                        print('Processo do TIPO IMPRESSÃO' + Fore.GREEN + ' criado com sucesso!' + Fore.WHITE)

            case 2: # Executar Próximo Processo
                pass
            
            case 3: # Executar Processo Específico
                pass
            
            case 4: # Salvar a Fila de Processos
                pass
            
            case 5: # Carregar do Arquivo a Fila de Processos
                pass
            
            case 6:
                processoImpressao = ProcessoImpressao(1)
                processoImpressao.execute()

            case 0: # Sair do Sistema
                MenuPrincipal.desligandoSistema() # Imprime Mensagens de Desligamento Dinâmicas
                break # Quebra o Loop do Menu Principal