"""
   TIPO LIST -- Mutável
   SUPORTA VALORES DE QUAISQUER TIPOS

   LIST = ARRAY
"""






"""
    CRIANDO UMA LISTA
"""
# lista1 = list()
# lista2 = []

# print(type(lista1), type(lista2))

# trabalho = ['Hermes Pardini', True, 'Tecnico de laboratório', 2, 2021]
# print(
# trabalho[2],
# trabalho[3])

# vida = list([1,2,3,4])
# print(vida)









"""
    MANIPULANDO UMA LISTA
    CRUD = Create, Read, Update, Delete
"""

# lista = [1, 2, 3, 4, 5, 6, 7]
# print(lista)

# lista[0] = 0 # MODIFICANDO NO ÍNDICE 0
# print(lista)

# del lista[0] # DELETANDO ÍNDICE
# print(lista)

# lista.append(8) # ADICIONA AO FINAL
# print(lista)

# lista.pop()
# print(lista) # REMOVE UM VALOR AO FINAL DA LISTA OU DO ÍNDICE ESCOLHIDO

# lista.insert(7, 20)
# print(lista)


# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b # concatenando listas
# print(lista_c, 'concatenando com sinal de +')

# lista_a.extend(lista_b)
# print(lista_a, 'Concatenada com a função Extend') # EXTEND MEXE NA LISTA 'A'

# lista_d = lista_a.copy() # COPIA A LISTA A PARA A VARIÁVEL D
# print(lista_d, 'LISTA A COPIADO PARA D')








"""
    UTILIZANDO FOR EM LISTA/ARRAY
"""

# familia = ['SANDRA', 'DEIVISON', 'DENIS', 'LÍVIA', 'DAVI']

# for i in familia:
#     print(i)





"""
    DESEMPACOTAMENTO
"""
def desempacotamento():
    print('DESENPACOTAMENTO')

    familia = ['SANDRA', 'DEIVISON', 'DENIS', 'LÍVIA', 'DAVI']

    a, b, c, d, e = familia
    for i in a, b, c, d, e:
        print(i)

    nome1, nome2, *_ = familia
    print(_) # RESTO

    _, nome2, _, *_ = familia
    print(_) # RESTO
    print(nome2)

    print('FIM DESEMPACOTAMENTO')
desempacotamento()





"""
    TUPLA - é IMUTÁVEL
    É UTILIZADO PARA REPRESENTAR VALORES QUE NÃO PODEM SER
    MODIFICADO. OU SEJA, POR ISSO É IMUTÁVEL.
"""

def tupla():
    print('----INÍCIO TUPLA----')

    nome = 'SANDRA', 'DEIVISON', 'DENIS', 'LÍVIA', 'DAVI'
    # nome1 = ('SANDRA', 'DEIVISON', 'DENIS', 'LÍVIA', 'DAVI')

    # print(nome[4])

    indice = range(len(nome))
    for i in indice:
        print(i, nome[i])

    
    """
        PARA NÃO UTILIZAR RANGE PARA ENUMERAÇÃO
        EU TENHO UMA FUNÇÃO enumerate()
    """

    for i in enumerate(nome):
        indice, nome = i
        print(i)



    print('----FIM TUPLA----')

# tupla()