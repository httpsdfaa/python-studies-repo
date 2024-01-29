print(12, 'Deivison', 2 + 2) # separação por padrão é espaço
print(52, 8, sep='-') # o separador agora é um -
print(20, 80, 60, 5, sep='/')

# Testar quebra de linha
print(50, 20, sep='-', end='++\r\n')
print(6, 8)

"""
    \r\n --> CRLF (Comum em windows )
    \n --> LF (Comum em Unix, Linux MacOs)
"""

# Caractere de Escape
print("Deivison \"Fernandes\"")
print('Deivison "Fernandes"') #código mais limpo e melhor para uso