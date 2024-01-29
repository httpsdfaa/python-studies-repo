"""
    ITERÁVEL --> str, range, etc (__iter__)
"""

# __ITER__() E ITER() SÃO A MESMA COISA.

texto1 = 'Deivison'.__iter__() # MÉTODO
# print(texto1)

texto2 = iter('Fernandes') # FUNÇÃO
# print(texto2)

"""
    __NEXT__() PRÓXIMO ou NEXT()
    ESSE MÉTODO ME DARÁ UM CARACTERE POR VEZ
"""
# print(texto1.__next__())
    


"""
    UTILIZANDO WHILE E FOR
"""
# while True:
#     try:
#         letra = next(texto1)
#         print(letra)
#     except StopIteration:
#         break

# for i in texto1:
#     print(i)

