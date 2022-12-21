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

Enumerate:
((0,'G'),(1,'e'),(2,'e'),(3,'k'),(4,' '),(5,'u'))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista 

for valor in enumerate(nome)
    
"""
"""
qtd = int(input('Quantas vezes esse loop deve rodar ?'))

for n in range(1,qtd+1):
    print(f'Imprimindo{n}')
    
qtd = int(input('Quantas vezes esse loop deve rodar ?'))
soma = 0

for n in range(1,qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

"""



