"""
Loop for

Loop -> Estrutura de repetição.
for -> Uma dessas estruturas

C ou Java

for(int i = 0 < 10; i++){
    //execução do loop
}

Python

for item in interavel
    //execução do loop

Utilizamos loops iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
-String
    nome = 'Geek University'
- Lista
    lista = [1,3,5,7,9,]
- Range
    numeros = range (1,10)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em um astring)
for letra in nome:
    print(letra)

# Exemplo de 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)
