from time import sleep

listaProcessos = []
listaProcessosCalculo = []
listaProcessosGravacao = []
class MenuPrincipal:
    def mainMenu():
        print('-'*50)
        print('''Digite o número da sua opção escolhida:
1 - Criar Processo
2 - Executar Próximo Processo
3 - Executar Processo Específico
4 - Salvar a Fila de Processos
5 - Carregar do Arquivo a Fila de Processos
0 - Sair do Sistema''')
        
    def opcoesProcessos():
        print('-'*50)
        print('''Digite o número da sua opção escolhida:
1 - Processo de Cálculo
2 - Processo de Gravação
3 - Processo de Leitura
4 - Processo de Impressão''')

    def opcoesOperador():
        print('-'*50)
        print('''Digite o número da sua opção escolhida:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
        
    def desligandoSistema():
        print('-'*50)
        print('Desligando o sistema...')
        sleep(1)
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')