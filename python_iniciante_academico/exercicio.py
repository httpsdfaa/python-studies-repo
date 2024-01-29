nome_in = input('Digite seu nome: ')
idade_in = input('Digite sua idade: ')

if nome_in != False or nome_in != '':
    print(f'Olá {nome_in}, seu nome invertido é {nome_in[::-1]}')
    if ' ' in nome_in:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome_in)} letras')
    print(f'A primeira letra do seu nome é {nome_in[0]}')
    print(f'A última letra do seu nome é {nome_in[-1]}')
else:
    print('Desculpe, você deixou campos vazios')

"""
    NÚMERO PAR OU ÍMPAR
"""
print('DIGITE UM NÚMERO INTEIRO PARA DESCOBRIR SE É ÍMPAR OU PAR')

num_in = input('Digite um número inteiro: ') 
num_in_float = float(num_in) # ACEITANDO VALORES FLOAT, POIS NÃO SEI QUAL NÚMERO O USUÁRIO IRÁ DIGITAR
num_in_int = None

MODULO_FLOAT = num_in_float % 1 # CHECAR SE O NÚMERO É UM FLOAT OU INTEIRO
FORMULA_PAR_IMPAR = num_in_float % 2 # CHECAR SE O NÚMERO É PAR OU ÍMPAR
NUM_INTEIRO = MODULO_FLOAT == 0 # CHECAR SE É UM NÚMERO INTEIRO
NUM_FLUTUANTE = MODULO_FLOAT != 0 # CHECAR SE É UM NÚMERO FLUTUANTE
NUM_PAR = FORMULA_PAR_IMPAR == 0 # CHECAR SE É IMPAR
NUM_IMPAR = FORMULA_PAR_IMPAR != 0 # CHECAR SE É PAR

if NUM_INTEIRO and NUM_PAR:
    num_in_int = int(num_in_float)
    print(f'{num_in_int} é um número par')
elif NUM_INTEIRO and NUM_IMPAR:
    num_in_int = int(num_in_float)
    print(f'{num_in_int} é um número ímpar')
elif NUM_FLUTUANTE:
    print(f'{num_in_float:.2f} é número flutuante. Digite um número inteiro')
else:
    print('Digite um número inteiro')


"""
    O CÓDIGO ACIMA TEM LÓGICA BOA, MAS TORNANDO DESNECESSÁRIAS ALGUMAS COISAS.
    VOU FAZER USO DE DE FUNÇÃO PARA REDUZIR A COMPLEXIDADE E TORNAR O CÓDIGO MAIS
    LEGÍVEL E LIMPO
"""

# isdigit() --> VERIFICA SE A ENTRADA É COMPOSTA POR DIGITOS NÚMERICOS
# is_integer() --> VERIFICA SE UM NÚMERO FLUTUANTE É INTEIRO.

NUM_IN = input('Digite um número inteiro: ')

if NUM_IN.isdigit():
    NUM_IN_FLOAT = float(NUM_IN)
    if NUM_IN_FLOAT.is_integer():
        NUM_IN_INT = int(NUM_IN_FLOAT)
        if NUM_IN_INT % 2 == 0:
            print(f'{NUM_IN_INT} é um número par.')
        else:
            print(f'{NUM_IN_INT} é um número ímpar.')
    else:
        print('Favor, digite um número inteiro')
else:
    print('Favor, digite um número inteiro')




"""
    QUAL SEU NOME?
"""

NOME_IN = input('QUAL O SEU PRIMEIRO NOME? ')

LEN_4 = len(NOME_IN) <= 4
LEN_6 = len(NOME_IN) > 4 and len(NOME_IN) <= 6
LEN_MAX = len(NOME_IN) > 6

if LEN_4:
    print('Seu nome é curto')
elif LEN_6:
    print('Seu nome é normal')
elif LEN_MAX:
    print('Seu nome é muito grande')
else:
    print('Favor, digite o seu nome')




"""
    EXIBA INDICES DAS LISTAS
"""

familia = ['fulano A', 'fulano B', 'fulano C', 'fulano D', 'fulano E']
familia.append('APPEND ADICIONADO')


range_len = range(len(familia)) # OUTPUT --> range(0, 5)

for i in range_len:
    print(i) # INDEX
    print(range_len) # range(0, 5)
    print(range_len[i]) # INDEX

    print(familia[i], i) # VALORES NO RESPECTIVO INDEX





"""
    FAÇA UMA LISTA DE COMPRAS COM ARRAY(LISTAS)
    O USUÁRIO DEVE TER POSSIBILIDADE DE
    INSERIR, APAGAR E LISTAR VALORES DA SUA LISTA
    NÃO PERMITA QUE O PROGRAMA QUEBRE COM ERROS DE 
    ÍNDICES ENEXISTENTES NA LISTAS
"""


def lista_compras():
    # VARIÁVEIS
    lista_compras = []

    # FUNÇÕES
    def VERIFICAR_TAMANHO_LETRA(minusc, maiusc, entrada):
        return entrada.lower() == minusc or entrada.upper() == maiusc

    def LISTA_COMPRAS():
        if lista_compras == []: 
            print('--SUA LISTA ESTÁ VAZIA--\n\n')
        else:
            print('LISTA DE COMPRAS\n')
            for indice, item in enumerate(lista_compras):
                print(f'{indice}: {item}')


        entrada_lista = input('\nVocê deseja adicionar item a lista? "S" ou  "N"->') # AÇÃO SE USUÁRIO DESEJA OU NÃO ADICIONAR ALGO A LISTA
        if VERIFICAR_TAMANHO_LETRA('s', 'S', entrada_lista):
            print('LISTA DE COMPRAS\n\n')
            INSERIR_COMPRAS()
        elif VERIFICAR_TAMANHO_LETRA('n', 'N', entrada_lista):
            main() # CHAMADA DA FUNÇÃO PRIMÁRIA PARA RECOMEÇAR A LÓGICA
        elif lista_compras == []:
            print('LISTAS DE COMPRAS ESTÁ VAZIO\n')
            LISTA_COMPRAS()
        else:
            print('\nESCOLHA UMA OPÇÃO VÁLIDA\n')
        
    def INSERIR_COMPRAS():
        i = 1
        while True:
            adicionar_valor_lista = input(f'{i}: ')
            if VERIFICAR_TAMANHO_LETRA('sair', 'SAIR', adicionar_valor_lista):
                return LISTA_COMPRAS()
            else:
                lista_compras.append(adicionar_valor_lista)

                i += 1
                continue
    def main():
        while True:
            entrada_in = input('L: Lista de compras \nI: Inserir item à lista de compras \n\
D: Apagar item da lista de compras \n-> ')
            nao_digito = not entrada_in.isdigit() # NÃO ACEITA SOMENTE NÚMEROS.
        
            if nao_digito and VERIFICAR_TAMANHO_LETRA('l', 'L', entrada_in):
                LISTA_COMPRAS()
            elif VERIFICAR_TAMANHO_LETRA('fechar', 'FECHAR', entrada_in):
                break
    main()
    
lista_compras()