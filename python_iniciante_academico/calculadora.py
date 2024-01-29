"""
    CALCULADORA
"""

print('CALCULADORA')

armazenar_valor = []
armazenar_operador = []

SOMA = '+'
SUBTRACAO = '-'
MULTIPLICACAO = '*'
DIVISAO = '/'

contador = 1
while True:
    ENT_VALOR = input(f'Digite o valor {contador}: ')

    if ENT_VALOR.isdigit():
        float(ENT_VALOR)
        armazenar_valor.append(ENT_VALOR)
    elif ENT_VALOR.isdigit() == False:
        print('DIGITE SOMENTE DÍGITOS NUMÉRICOS')
        continue

    print('\n')
    ENT_OPERADOR = input('SOMA: (+)  SUBTRAÇÃO: (-)  MULTIPLICAÇÃO: (*)  DIVISÃO: (/)  : ')

    if ENT_OPERADOR.isdigit() == False:
        if ENT_OPERADOR == '+' or ENT_OPERADOR == '-' or ENT_OPERADOR == '/' or ENT_OPERADOR == '*':
            armazenar_operador.append(ENT_OPERADOR)
        elif ENT_OPERADOR == '':
            print('DIGITE ALGUM OPERADOR')
            continue
        else:
            print('DIGITE SOMENTE OPERADORES MATEMÁTICOS')
            continue
    else:
        ...
        
    print('\n')

    print(armazenar_valor, armazenar_operador)
   
    
    contador += 1