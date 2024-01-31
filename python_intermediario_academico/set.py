"""
    Sets - Conjuntos em Python (Type set)
    Conjuntos são ensinados na matemática

    Representados graficamente pelo o diagrama de Venn
    Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno



    Sets são eficientes para remover valores duplicados de iteráveis

    - VALORES DE SET SERÃO SEMPRE ÚNICOS
    - NÃO ACEITAM VALORES MÚTAVEIS
    - NÃO POSSUÍ ÍNDEXES
    - NÃO GARANTE ORDEM
    - SÃO ITERÁVEIS (for, in, not in)
"""

# CRIANDO UM SET
# UM SET NÃO É UM DICT (DICIONÁRIO)
s1 = set()
print(type(s1))

s2 = set('Guido')
print(s2) # iterável


# Removendo valores duplicados de iteraveis
# LEMBRANDO, OS SETS NÃO GARANTE ORDEM
list_example = [1, 2, 2, 3, 3, 3, 2, 1, 9, 10, 1, 1] # repetindo valores para remover em na class set
s3 = set(list_example) # removeu todos os valores repetidos
print(s3)




"""
    MÉTODOS ÚTEIS:
    add, update, clear, discard
"""
s4 = set()
s4.add('Guidoooooo')
s4.add('Vannnnnnnnnn')
s4.add('Rossummmmmmmmmmmm') 

s4.update((50, 100, 150)) # envia varios valores para o set

s4.discard(50) # descarta valores. Como não existe index, teremos que utilizar o próprio valor para descarte
s4.discard(100)
s4.discard(150)

# s4.clear() # limpa o set

print(s4)




"""
    OPERADORES ÚTEIS:
    união | união  (union) - une
    intersecção & (intersection) - Itens presentes em ambos
    diferença - Itens presentes apenas no set da esquerda
    diferença simétrica ^ - Itens que não estão em ambos
"""
a = {1, 2, 3}
b = {2, 3, 4}

x = a | b # união
print(x)

y = a & b # intersecção
print(y)

z = a - b # diferença. Ou seja, valores presentes somente no set da esquerda
print(z)

w = a ^ b # valores que está presente em um conjunto, mas não está presente em outro e vice-versa
print(w)