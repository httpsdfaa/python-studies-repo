""" 
    Por padrão função em Python retornam None
"""

def funcao():
    # código
    ...












""" 
    ARGUMENTO NOMEADO E NÃO NOMEADO
"""

def divisao(x, y):
    print(f'{x=} {y=} | {x / y = }')


# ARGUMENTOS NÃO NOMEADO(posicionais), A ORDEM IMPORTA. EXEMPLOS ABAIXO
print('Argumentos não nomeados\n')
divisao(10, 2) # 10 = X e Y = 2
divisao(2, 10) # 2 = Y e X = 10

#ARGUMENTOS NOMEADOS A ORDEM NÃO IMPORTA
print('Argumentos nomeados\n')
divisao(y=2, x=10)
divisao(x=10, y=2)












"""
    EMPACOTAMENTO E DESEMPACOTAMENTO
"""

# LEMBRETE DE DESEMPACOTAMENTO
x, y, *resto = 1, 2, 3, 4, 5
print(f'Desempacotamento: {x, y, resto}')

def multiplo_argumento(*args):
    return args

print(multiplo_argumento(1,2,3,4,5,6,7,8)) # retorna uma tupla

# CALCULO SOMA
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 8 # uma tupla
print(numeros) # empacotado
print(*numeros) # DESempacotado 

"""
    HIGHER ORDER FUNCTIONS - FUNÇÕES QUE PODEM RECEBER E/OU RETORNAR OUTRAS FUNÇÕES
    FUNÇÕES DE PRIMEIRA CLASSE - FUNÕES QUE SÃO TRATADAS COMO OUTROS TIPO DE DADOS COMUNS(STRINGS, INTEIROS, ETC...)
"""







""" 
    CLOUSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # ARMAZENANDO O RETORNO DA FUNÇÃO NA MEMORIA. POR ESSE MOTIVO EU NÃO EXECUTEI COM OS PARENTESES


s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

print(s1) # A SAIDA É ONDE A FUNÇÃO ESTÁ ARMAZENADA NA MEMORIA
print(s2) # A SAIDA É ONDE A FUNÇÃO ESTÁ ARMAZENADA NA MEMORIA

print(s1('Deivison')) # CLOUSURE
print(s2('Deivison')) # CLOUSURE

familia = ['Sandra', 'Denis', 'Deivison', 'Livia', 'Davi']

for nome in familia:
    print(s1(nome)) # CLOUSURE
    print(s2(nome)) # CLOUSURE