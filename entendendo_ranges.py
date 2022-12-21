"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
_ Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória mas sim de maneira especificada.
formas gerais :

renge(valor_de_parada)
obs: Valor_de_parada não inclusive (início padrão 0, e passa de 1em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)
"""
"""
# Forma 2 

 range(valor_de_inicio, valor_de_parada)

 OBS: valor_de_parada não inclusive(início especificado pelo usuário, e passo de 1 em 1)
for num in range(1, 11):
    print(num)
    
# forma 3 
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(5, 55, 5):
    print(num)

# forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(10, -1, -1):
    print(num)
     
"""
