from cryptography.fernet import Fernet
import random
import string
import re
print('\n')
print('-*-' * 5,'Gerador De Senhas', 5 * '-*-')
mestre = 'S'
while mestre != 'N':
    print('''
    insira para:
        [1] gerar uma senha nova 
        [2] consultar uma senha criada
        [3] criptografar senhas salvas
        [4] descriptografar as senhas e pesuisar 
    ''')
    senhamestre = int(input('O que você deseja: '))
    if senhamestre == 1:
        senha = 'S'
        while senha != 'N':
            nome = str(input('Digite seu nome: ')).lower().replace(" ", "")
            print('''Escolha a opção:
                1- Gerar senha automatica 
                2- Inserir palavra(s)''')
            opçao = int(input('Qual opção: '))
            #caracteres = string.ascii_letters + string.digits + string.punctuation
            caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
            if opçao == 1:
                print('''Escolha a opção da quantidade de caracteres:
                    1- 8 
                    2- 12 
                    3- 14 
                    4- 16''')
                qtd = int(input('Qual opção: '))
                if qtd == 1:
                    qtd1 = []
                    for _ in range(8):
                        qtd1.append(random.choice(caracteres))
                    qtd1_juncao = ''.join(qtd1)
                    print(f'Senha: {qtd1_juncao}')
                    with open('SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtd1_juncao}\n')
                elif qtd == 2:
                    qtd2 = []
                    for i in range(12):
                        qtd2.append(random.choice(caracteres))
                    qtd2_juncao = ''.join(qtd2)
                    print(f'Senha: {qtd2_juncao}')
                    with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtd2_juncao}\n')
                elif qtd == 3:
                    qtd3 = []
                    for _ in range(14):
                        qtd3.append(random.choice(caracteres))
                    qtd3_juncao = ''.join(qtd3)
                    print(f'Senha: {qtd3_juncao}')
                    with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtd3_juncao}\n')
                elif qtd == 4:
                    qtd4 = []
                    for _ in range(16):
                        qtd4.append(random.choice(caracteres))
                    qtd4_juncao = ''.join(qtd4)
                    print(f'Senha: {qtd4_juncao}')
                    with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtd4_juncao}\n')
                else:
                    print('Opção invalida! Escolha um número entre 1 e 4')
            elif opçao == 2 :
                nome1 = 'jose'
                palavra = 'jose'
                while palavra == nome1:        
                    print('Atenção!!! Evitar informações pessoais: Não use seu nome, data de nascimento ou palavras comuns. ')
                    palavra = str(input('Insira a(s) palavra(s): ')).lower().replace(" ", "")
                    caracteres2 = palavra + palavra.upper() + '0123456789!@#$%&'
                    nnome = re.escape(nome)
                    nome1 = nome
                    if re.search(nnome, palavra):
                            print(f'A palavra {palavra} é igual ao seu nome {nome}. Por favor, digite outra palavra.')
                    else:
                        print('''Escolha a opção da quantidade de caracteres:
                        1- 8 
                        2- 12 
                        3- 14 
                        4- 16''')
                        qtdd = int(input('Qual a opção: '))
                        if qtdd == 1 :
                            qtdd1 = []
                            for i in range(8):
                                qtdd1.append(random.choice(caracteres2))
                            qtdd1_juncao = ''.join(qtdd1)
                            print(f'Senha: {qtdd1_juncao}')
                            with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtdd1_juncao}\n')
                        elif qtdd == 2 :
                            qtdd2 = []
                            for i in range(12):
                                qtdd2.append(random.choice(caracteres2))
                            qtdd2_juncao = ''.join(qtdd2)
                            print(f'Senha: {qtdd2_juncao}')
                            with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtdd2_juncao}\n')
                        elif qtdd == 3 :
                            qtdd3 = []
                            for i in range(14):
                                qtdd3.append(random.choice(caracteres2))
                            qtdd3_juncao = ''.join(qtdd3)
                            print(f'Senha: {qtdd3_juncao}')
                            with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtdd3_juncao}\n')
                        elif qtdd == 4 :
                            qtdd4 = []
                            for i in range(16):
                                qtdd4.append(random.choice(caracteres2))
                            qtdd4_juncao = ''.join(qtdd4)
                            print(f'Senha: {qtdd4_juncao}')
                            with open(f'SenhasSalvas.txt', 'a', encoding='utf-8') as arquivo: arquivo.write(f'{nome}: {qtdd4_juncao}\n')
                        else:
                            print('Opção invalida! Escolha um número entre 1 e 4')
            else:
                print('Opção invalida! Escolha a opção desejada 1 ou 2.')
            senha = str(input('Deseja gerar outra senha [S/N]? ')).upper()
    elif senhamestre == 2:
        nomeproc = str(input('Digite o nome que deseja procurar a senha: ')).strip().lower()
        with open('SenhasSalvas.txt', 'r', encoding='utf-8') as arquivo: linhas = arquivo.readlines()
        encontrado = False
        for linha in linhas:
            partes = linha.strip().split(":")
            if len(partes) == 2 and partes[0].strip().lower() == nomeproc:
                print('Resultado encontrado: ')
                print(linha.strip())
                encontrado = True
        if not encontrado:
            print('Nome não encontrado no arquivo. Tente outro!')
    elif senhamestre == 3:
        chave = Fernet.generate_key()
        with open('ChaveSegurança', 'wb') as chaveArquivo: chaveArquivo.write(chave)
        fernet = Fernet(chave)
        with open('SenhasSalvas.txt', 'rb') as arquivoOriginal: dados = arquivoOriginal.read()
        dadosCript = fernet.encrypt(dados)
        with open('SenhasCript.txt', 'wb') as arquivoCript: arquivoCript.write(dadosCript)
        print('Arquivo criptografado com suceso!')
    elif senhamestre == 4:
        with open('chaveSegurança', 'rb') as chaveArquivo: chave = chaveArquivo.read()
        fernet = Fernet(chave)
        with open('senhasCript.txt', 'rb') as arquivoCript: dadosCript = arquivoCript.read()
        dados = fernet.decrypt(dadosCript).decode()
        print('Conteúdo descriptografado.')
        nomeproc1 = str(input('Digite o nome que deseja procurar a senha: ')).strip().lower()
        linhas = dados.split('\n')
        encontrado = False
        for linha in linhas:
            partes = linha.strip().split(":")
            if len(partes) == 2 and partes[0].strip().lower() == nomeproc1:
                print('Resultado encontrado: ')
                print(linha.strip())
                encontrado =True
            if not encontrado:
                print(f'Nome "{nomeproc1}" não encontrado no arquivo. Tente outro!')
    else:
        print('Opção invalida!')
    mestre = str(input('Deseja continuar [S/N]? ')).upper()
print('Operação finalizada!')
