"""
    EXERCICIOS COM FUNÇÕES

    CRIE UMA FUNÇÃO QUE MULTIPLICA TODOS OS ARGUMENTOS
    NÃO NOMEADOS RECEBIDOS
    RETORNE O TOTAL PARA UMA VARIÁVEL E MOSTRE O VALOR DA VARIÁVEL

    CRIE UM FUNÇÃO QUE FALA SE O NÚMERO É PAR OU IMPAR.
    RETORNE SE O NUMERO É PAR OU IMPAR
"""

def multiplicacao(*args):
    total = 1 
    for numero in args:
        total *= numero # multiplicar

    return total

resultado = multiplicacao(4, 2)
print(resultado)

def impar_par(valor):
    
    impar = (valor % 2) != 0
    par = (valor % 2) == 0
    resultado = 0

    if par:
        resultado = f'{valor} é PAR'
    elif impar:
        resultado = f'{valor} é ÍMPAR'
    else:
        print('ALGO ACONTECEU')

    return resultado

impar_ou_par = impar_par(5)
print(impar_ou_par)




"""
    CRIE FUNÇÕES QUE DUPLICAM, TRIPLICAM E QUADRUPLICAM
    O NUMERO RECEBIDO COMO PARÂMETRO
"""

def crie_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = crie_multiplicador(2)
triplicar = crie_multiplicador(3)
quadruplicar = crie_multiplicador(4)

print(duplicar(2)) # output 4
print(triplicar(2)) # output 6
print(quadruplicar(2)) # output 8