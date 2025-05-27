'''
gerar senhas automaticas. Deve ter letras maiusculas, minusculas, caracteris especiais e números
com escolha do usuário para enserir uma palavra ou mais para gerar em cima desse
e escolha da quantidade de caracteis sendo no mínimo 8, 12, 14 ou 16 
Israel

'''
import random
import string
import datetime
print('\n')
print('-*-' * 5,'Gerador De Senhas', 5 * '-*-')
nome = str(input('Digite seu nome: '))
nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
nascfor = nascimento.strftime("%d de %B de %Y")
print('Escolha a opção desejada: 1- Gerar senha automatica ou 2- Inserir palavra(s)')
opçao = int(input('Qual opção: '))
#caracteres = string.ascii_letters + string.digits + string.punctuation
caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
if opçao == 1:
    print('Escolha a opção dejada da quantidade de caracteres: 1- 8 ; 2- 12 ; 3- 14 ou 4- 16')
    qtd = int(input('Qual opção: '))
    if qtd == 1:
        qtd1 = []
        for _ in range(8):
            qtd1.append(random.choice(caracteres))
        qtd1_juncao = ''.join(qtd1)
        print(f'Senha: {qtd1_juncao}')
    elif qtd == 2:
        qtd2 = []
        for i in range(12):
            qtd2.append(random.choice(caracteres))
        qtd2_juncao = ''.join(qtd2)
        print(f'Senha: {qtd2_juncao}')
    elif qtd == 3:
        qtd3 = []
        for _ in range(14):
            qtd3.append(random.choice(caracteres))
        qtd3_juncao = ''.join(qtd3)
        print(f'Senha: {qtd3_juncao}')
    elif qtd == 4:
        qtd4 = []
        for _ in range(16):
            qtd4.append(random.choice(caracteres))
        qtd4_juncao = ''.join(qtd4)
        print(f'Senha: {qtd4_juncao}')
    else:
        print('Opção invalida! Escolha um número entre 1 e 4')
elif opçao == 2 :
    print('Atenção!!! Evitar informações pessoais: Não use seu nome, data de nascimento ou palavras comuns. ')
    palavra = str(input('Insira as palavra(s) desejada(s): ')).lower().replace(" ", "")
    caracteres2 = palavra + palavra.upper() + '0123456789!@#$%&'
if palavra != nome:
    print('Escolha a opção desejada de quantidade de caracteres: 1- 8 ; 2- 12 ; 3- 14 ou 4- 16')
    qtdd = int(input('Qual a opção: '))
    if qtdd == 1 :
        qtdd1 = []
        for i in range(8):
            qtdd1.append(random.choice(caracteres2))
        qtdd1_juncao = ''.join(qtdd1)
        print(f'Senha: {qtdd1_juncao}')
    elif qtdd == 2 :
        qtdd2 = []
        for i in range(12):
            qtdd2.append(random.choice(caracteres2))
        qtdd2_juncao = ''.join(qtdd2)
        print(f'Senha: {qtdd2_juncao}')
    elif qtdd == 3 :
        qtdd3 = []
        for i in range(14):
            qtdd3.append(random.choice(caracteres2))
        qtdd3_juncao = ''.join(qtdd3)
        print(f'Senha: {qtdd3_juncao}')
    elif qtdd == 4 :
        qtdd4 = []
        for i in range(16):
            qtdd4.append(random.choice(caracteres2))
        qtdd4_juncao = ''.join(qtdd4)
        print(f'Senha: {qtdd4_juncao}')
    else:
        print('Opção invalida! Escolha um número entre 1 e 4')
else:
    print('A palavra inserida não pode ser igual ao seu nome, tente novamente!')
