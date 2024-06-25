# Empacotamento e desempacotamento

a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Alice',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 22,
    'altura': 1.7
}



a, b = pessoa
print(a, b) # retorna keys

a, b = pessoa.values() # retorna values
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

print("UTILIZANDO FOR \n\n")
for chave, valor in pessoa.items():
    print(chave, valor)



# EXTRAINDO DADOS DE UM DICT COM ** e adicionando em um dict vazio
pessoa_completa = {}
pessoa_completa = {**pessoa}

print(pessoa_completa, '\n')

# extraidno e fazendo nova adição
pessoa_completa = {**pessoa, 'nova chave': 'novo valor'}
print(pessoa_completa, '\n')


# args e kwargs
# args(*) (já vimos em funções)
# kwargs(**) - keyword arguments ( argumentos nomeados )
def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs) # nomeado
    print(args) # não nomeado

mostro_argumentos_nomeados(nome='Deivison', sobrenome='Fernandes')
mostro_argumentos_nomeados(1, 2, 3, 4, 5)