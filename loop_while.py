"""
Loop while
Forma geral

while expressão _booleana:
//execução do loop

O bloco de while será repetido enquanto a expressão booleana for verdadeira.
Expressão Booleana é toda expressão onde o resultado é verdadeira ou falsa.
Exemplo:

num = 5

num < 5

#exemplo 1

numero = 1
while numero < 10:
    print(numero)
    # numero = numero + 1

######
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# obs: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

"""

# Exemplo 2

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica: ')
