print('\n')
print('-*-' * 5,'Minha Contabilidade', 5 * '-*-')
menuMestre = 1
while menuMestre != 0:
    print('''
        Insira para:
          [1] Adicionar conta
          [2] Pesquisar conta
          [3] Orçamento
          [0] Sair
        ''')
    menuMestre = int(input('opção: '))
    if menuMestre == 1:
        print('Adicionar Entradas ou Saídas')
    elif menuMestre == 2:
        print('Pesquisar contas de Entrada ou Saída')
    elif menuMestre == 3:
        print('Criar Orçamento para saber se é viavel fazer uma compra')
    else:
        print('Opção Invalida! Opções aceitas [1, 2, 3 ou 0]')
print('Fim!')