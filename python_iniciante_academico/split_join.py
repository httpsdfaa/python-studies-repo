""" 
    split e join com list e str
    split - divide
    join - une
    strip - limpa espaços
"""

frase = 'Eu quero aprender IA e Machine Learning'
split_frase = frase.split(' ') 
print(frase)
print(split_frase)

join_frase = ' '.join(split_frase) # Juntando a frase e mantendo espaços como separação
print(join_frase)