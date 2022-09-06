# Eu vou fazer uma agenda

# Importações
import sqlite3
from sqlite3 import Error
from time import sleep

# Criando conexão
try:
    
    conexão = sqlite3.connect("C:/Users/angel/OneDrive/Ambiente de Trabalho/About programation/Python Curso 2/exercícios/bank.db")

except:

    print(Error)

# Funções
def inserir(conexão):

    id = input('Digite um id para esse compromisso: ')

    compromisso = input('Descreva a compromisso, e se quiser adicione a hora: ')

    cursor = conexão.cursor()

    cursor.execute(f"""INSERT INTO tb_agenda
                (id_compromisso, compromisso)
            VALUES('{id}',  '{compromisso}')""")

    conexão.commit()

def deletar(conexão):

    id = input('Digite o id do compromisso: ')

    cursor = conexão.cursor()

    cursor.execute(f"DELETE FROM tb_agenda WHERE id_compromisso='{id}'")

    conexão.commit()

def editar(conexão):
    
    compromisso = input('Digite o antigo compromisso: ')
    compromisso2 = input('Novo compromisso: ')

    cursor = conexão.cursor()

    cursor.execute(f"UPDATE tb_agenda SET compromisso='{compromisso}' WHERE compromisso='{compromisso2}'")

    conexão.commit()

def mostrar_tudo(conexão):

    cursor = conexão.cursor()

    cursor.execute(f"SELECT * FROM tb_agenda")

    res = cursor.fetchall()

    return res

def mostrar_individual(conexão):
    
    id = input('Id do compromisso: ')

    cursor = conexão.cursor()

    cursor.execute(f"SELECT * FROM tb_agenda WHERE id_compromisso='{id}'")

    res = cursor.fetchall()

    return res

# Colocando para funcionar
print('----Agenda----')
print('Escolha uma opção: ')
print('1 - Inserir novo compromisso')
print('2 - Deletar compromisso')
print('3 - Editar compromisso')
print('4 - Mostrar compromissos')
print('5 - Mostrar compromisso expecífico')

# Ifs, elifs e elses
while True:

    try:

        opção = int(input('Qual opção você escolhe? '))

        if opção == 1:
            inserir(conexão=conexão)
            print('Feito.')
        
        if opção == 2:
            deletar(conexão=conexão)
            print('Feito.')
        
        if opção == 3:
            editar(conexão=conexão)
            print('Feito.')

        if opção == 4:
            re = mostrar_tudo(conexão=conexão)
            for r in re:
                print(f'{r[0]} = {r[1]}')
        if opção == 5:
            resul = mostrar_individual(conexão=conexão)
            for r in resul:
                print(f'{r[0]} = {r[1]}')
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

        if res in 'S':
            continue
        elif res in 'N':

            break
        else:

            print('\033[31mDigite um caractér válido!\033[m')
    except Error:
        print(Error)

print('««FINALIZADO»»')
