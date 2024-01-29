print(1 + 1 == 2)
print(True != False)

print(int('1')) # CONVERTENDO STRING PARA INTEIRO
print(int('1') + 1)
print(str(1502) + 'Deivison') # ONVERTENDO INTEIRO EM STRING E CONCATENANDO STRING
print(bool(' '))

"""
    CONVERSÃO DE TIPOS, COERSÃO, TYPE CONVERTION, TYPECASTING, COERCION ( ATOS DE CONVERSÃO DE TIPOS )
"""

"""
    VARIAVEL, MODULO E DIVISÃO INTEIRA
"""

nome_var =  'Deivison Fernandes'
idade_var = 84
data_nascimento_dia = 5
data_nascimento_mes = 5
data_nascimento_ano = 1950

print(nome_var, idade_var, end=" ") #OUTPUT --> Deivison Fernandes x
print(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano, sep="/", end=".")


exponenciacao = 3 ** 3 
modulo = 2 % 5 # Resto da divisao
divisao_inteira = 5 // 2

print(
    'Exponenciação:', exponenciacao,
    'Modulo:', modulo,
    'Divisão inteira:', divisao_inteira
)


"""
    CONCATENAÇÃO
"""

deivison3x = 'Deivison ' * 3
print(deivison3x)

concatenacao = 'Deivison' + ' ' + 'Fernandes'
print(concatenacao)


"""
    CÁLCULO IMC
"""

nome = 'Deivison'
altura = 1.73
peso = 73.0

imc = format(73 / (1.73 ** 2), '.1f') # FORMAT = ARREDONDAMENTO
print(imc)
print(...) # ELLIPSIS (usada para assumir um valor none")


"""
    f-strings
"""

nome = 'Deivison'
idade = 25
nascimento = '01/01/1111'
altura = 1.7310
historia = f'ele tem {idade} anos de idade e nasceu {nascimento} e sua altura é de {altura:.2f}'

# print('Deivison Fernandes é um técnico de laboratório que está estudando para ser um programador', historia)

print(len(nome))
print(nome[9:0:-1]) # Inicio : Final : Quantas casas


"""
    FORMATANDO STRING COM METODO FORMAT
        Tudo em Python é OBJETO
"""
a = 'Abacate'
b = 'Bolacha'
c = 25

formato = 'A = {}, B = {}, C = {}'.format(a, b, c)

print(formato)

"""
    INTERPOLAÇÃO DE STRINGS
    s --> String
    f --> Float
    d e i --> Int
    x e X --> Hexadecimal
"""

nome = 'CB300r'
valor = 10000
variavel = '%s, tem um valor de %d' %(nome, valor)

print(variavel)

