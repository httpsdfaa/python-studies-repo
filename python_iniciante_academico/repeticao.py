# contador = 0
# contadorNeg = 4

# while contador <= 4:
#     input('Qual o seu nome? ')
#     print(f'{contador}')

#     contador += 1 # INCREMENTO --> contador = contador + 1

# print('FIM')

# while contadorNeg >= 0:
#     input('Qual seu nome? ')
#     print(f'{contadorNeg}')

#     contadorNeg -= 1
# print('FIM')

"""
    VARIAVEL = VARIAVEL + 1
    VARIAVEL += 1 # Forma simplificada

    VALE PARA TODOS OS OPERADORES NUMÉRICOS
        -=      subtração
        *=      multiplicação
        /=      divisão
        //=     divisão inteira
        %=      módulo
        **=     exponenciação

"""

"""
    BREAK --> Quebra o laço
"""

# contador = 0
# while contador < 50:
#     print(contador +1)

#     contador += 1

#     if contador == 20:
#         break # PARA O LAÇO QUANDO FOI VERDADE


"""
    CONTINUE --> Oposto de BREAK
"""

# contador = 0
# while contador < 50:
#     contador += 1

#     if contador == 20:
#         print('CONTINUE SENDO EXECUTADO')
#         continue

#     print(f'{contador}')

#     if contador == 40:
#         break


# contador = 0
# contadorx = 0

# while contador < 50:
#     print('Print externo')

#     while contadorx < 10:
#         print('PRINT INTERNO')

#         contadorx += 1


#     if contador == 20:
#         break

#     contador += 1

"""
    CONTADOR COM STRING
"""
# contador = 0
# nome = input('Digite seu nome: ')
# nome_len = len(nome)

# while contador < nome_len:
#     print(nome[contador])

#     contador += 1


"""
    REPETIÇÃO FOR / IN
"""

# nome = 'deivison'
# for i in nome:
#     print(i)


"""
    FOR + RANGE
    range --> range(start, stop, step)
"""

# print(range(10))
# print(range(5, 10))
# print(range(1, 10, 2))

# numeros = range(0, 10, 2) # INÍCIO, PARAR, PULAR

# for i in numeros:
#     print(i)

for i in range(10):
    print(i)
    if i == 2:
        print('Continuando...')
        continue

    if i == 8:
        print('Pulando...')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo..')
    
