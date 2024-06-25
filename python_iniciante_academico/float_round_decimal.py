""" 
    Imprecisão de ponto flutuante
    Doble-precision floating-point forma IEEE 754
"""

num_1 = 0.1
num_2 = 0.789
num_3 = num_1 + num_2

print(num_3) # imprecisso
print(f'{num_3:.2f}') # solucao string
print(round(num_3, 2)) # solucao por funcao numero 