# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

print(list(range(1, 11))) # forma de criar uma lista 1

# forma de criar lista 2
lista = []
for numero in range(1, 11):
    lista.append(numero)

print(lista)

# LIST COMPREHENSION
lista_a = [numero+1 for numero in range(10)]
print(lista_a)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [produto for produto in produtos]
print(*novos_produtos, sep='\n')

# Pegando valores na própria sintaxe
novos_produtos = [ {'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos ]
print(novos_produtos)