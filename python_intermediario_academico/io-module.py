"""
    Existem 3 tipos de principais de I/O
    -- text I/O
    -- binary I/O
    -- raw I/O
"""

# open() -- file object

"""
    LEGENDA:
    -r leitura
    -w writing
    -x criação exclusiva, falhando caso o arquivo já exista
    -a writing, appeding to the end of file if it exists
    -b binary mode
    -t text mode
    '+' updating (read and writing)
"""

names = ['Python', 'Python2', 'Python3', 'Python4', 'Python5']

# for para escrever('w' - Writing) o todos os valores da lista names
with open('python-file-example.txt', 'w', encoding='utf-8') as file_w:
    for name_index in names:
        file_w.write(f'{name_index} -- ESCREVENDO COM "w" \n')


names = ['Python', 'Python2', 'Python3', 'Python4', 'Python5']

# utilizando escrever com 'a', para incrementar novos valores no arquivo sem mexer com antigo
with open('python-file-example.txt', 'a', encoding='utf-8') as file_a:
    for name_index2 in names:
        file_a.write(f'{name_index2} -- ESCREVENDO COM "a" \n')


"""
O CODIGO ABAIXO É O MESMO DE CIMA, O QUE MUDOU FOI IMPLEMENTAR O OPEN COM VARIÁVEL CONVENCIONAL

w = open('python-file-example.txt', 'w', encoding='utf-8')
for name_index in names:
    w.write(f'{name_index}\n')

"""

