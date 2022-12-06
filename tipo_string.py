"""
Tipo string
EM python , um dado é considerado do tipo string sempre que:
- EStiver entre àspas simples -> 'uma string', '234','a','True','42.3'
- EStiver entre àspas dupla -> "uma string", "234","a","True","42.3"
- EStiver entre àspas simples triplas -> '''uma string''', '''234''','''a''','''True''','''42.3'''

nome = "Geek University"
print(nome)
print(type(nome))

nome = "Geek \nUniversity"
print(nome)
print(type(nome))

nome = "Geek University"
print(nome.upper())

nome = "Geek University"
print(nome.lower())

nome = "Geek University"
print(nome.split())  # transforma uma lista de strings
......................................................
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# ['G','E','E','K', '', 'U','N','I','V','E','R','S','I','T','Y',]

nome = "Geek University"
d = "dracula"
print(nome[0:4])

print(nome[5:15])

#[0,    1]
#['GEEK','UNIVERSITY']
print(nome.split()[0])

print(nome.split()[1])

print(nome[::])
print(nome[::-1])
print(d[::-1])
.........................................
"""
# EStiver entre àspas duplas triplas -> """uma string""", """234""","""a""","""True""","""42.3"""


nome = "Fabio magalhães"
d = "dracula"
print(nome[0:4])

print(nome[5:15])

#[0,    1]
#['Fabio','Magalhaes']
print(nome.split()[0])

print(nome.split()[1])

print(nome[::])
print(nome[::-1])




