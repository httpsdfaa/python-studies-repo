"""
    Dicionários em Python (tipo dict)

    Dicionários são estruturas de dados do tipo par 
    de "key" e "value"

    Chaves podem ser consideradas como o "index"
    que vimos na lista e podem ser de tipos imutáveis
    como: str, int, float, bool, tuple, etc.

    O valor pode ser de qualquer tipo, incluindo outro dicionário

    Utilizamos as chaves - {} - ou a classe dict para criar 
    dicionários.

    Imutáveis: str, int, float, bool, tuple
    Mutável: dict, list

    person = {
        'name': 'Guido',
        'surname': 'van Rossum',
        'born': '31-01-1956',
        'address': [
            {'street': 'tal tal', 'number': 0101},
            {'street': 'tal2 tal2', 'number': 0202}
        ]
    }

"""

# DICTIONARY (dict)
person = {
    'name': 'Guido',
    'surname': 'van Rossum',
    'born': '31-01-1956',
    'address': [
        {'street': 'tal tal', 'number': 10},
        {'street': 'tal2 tal2', 'number': 20}
    ]
}

print(type(person))


# UTILIZANDO A FUNÇÃO CLASS DICT
# CONSTRUÇÃO MENOS UTILIZADA
person_class = dict(
    name='Guido',
    surname='van Rossum',
    born='31-01-1956'
)

print(type(person_class))


# ACESSANDO OS VALORES DO DICT
print(person['name'])

for chave in person:
    print(chave, person[chave])




# MANIPULANDO CHAVES E VALORES EM DICT
manipulate = {}

manipulate['key_1'] = 'Adicionado'
print(manipulate)

manipulate['key_1'] = 'Alterado'
print(manipulate)

del manipulate['key_1']
print(manipulate)


# TRATANDO EXCESSÃO CASO UMA KEY NÃO EXISTA
print(manipulate.get('key_not_exist', 'Chvave não existe'))




"""
    MÉTODOS SÃO BLOCOS DE CÓDIGOS ASSOCIADOS A OBJETOS

    MÉTODOS úteis dos Dicts em Python
    len - Quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    items - iterável com chaves e valores
    setdefault - Adiciona valor se a chave não existe
    copy - retorna uma cópia rasa (shallow copy), não copia valores em subníveis
    import copy - x.deepcopy(var) - faz uma cópia profunda e acessando os subníveis
    get - obtém uma chave
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último item adicionado
    update - Atualiza um dict com outro
"""

dict_example = {
    'key1': 'Valor 1',
    'key2': 'Valor 2',
    'key3': 'Valor 3'
}

print(dict_example.__len__(), '\n') # quantidade de chaves
print(dict_example.keys(), '\n') # iterável com as chaves
print(dict_example.values(), '\n') # iterável com os valores
print(dict_example.items(), '\n') # retorna chave com o valor
for chave, valor in dict_example.items():
    print(chave, valor)

print(dict_example.setdefault('key_adicionada', 'Valor adicionado'), '\n')

dict_example_copy = dict_example.copy() # valor copiada

# VALOR EXCLUIDO SOMENTE NO DICT_EXAMPLE_COPY
# Mas, não exluído na variável original
del dict_example_copy['key3']
print(dict_example_copy, '\n')
print(dict_example), '\n'

print(dict_example.pop('key1'), '\n')
print(dict_example, '\n')

print(dict_example.popitem(), '\n')
print(dict_example, '\n')

print(dict_example.update({
    'key2':'valor atualizado'
}), '\n')
print(dict_example)