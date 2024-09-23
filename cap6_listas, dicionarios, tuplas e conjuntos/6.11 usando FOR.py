""" 
Python apresenta uma estrura de repetição especialmente projetada para percorrer sequências em uma lista, tupla, string ou qualquer outro iterável. Essa estrutura é o FOR.   

funciona semelhante ao while, mas é mais simples de usar. Mas a cada iterção, o FOR atribui o próximo valor da sequência à variável de controle. Quando a sequência termina, o loop termina também. 

Exemplo1:

L = [1, 2, 3, 4, 5]

for i in L:
    print(i)

1. quando for executado, o FOR atribui o primeiro valor da lista à variável i.
no caso, o valor 1. L[0] = 1; i = 1 
                    L[1] = 2; i = 2 E ASSIM POR DIANTE.
                
                
2. quando o FOR termina de percorrer a lista, ele termina o loop.

3. o FOR pode ser usado para percorrer qualquer sequência, como strings, tuplas, listas, etc.

4. o FOR também pode ser usado para percorrer sequências numéricas, usando a função range().

5. a função range() gera uma sequência de números, começando em 0 por padrão, e incrementando em 1 (por padrão), e terminando em um número especificado. 

Exemplo2: 

L = [1, 2, 3, 4, 5]
x = 0

while x < len(L):
    i = L[x]
    print(i)
    x += 1
    
1. quando for executado, o WHILE verifica se x é menor que o tamanho da lista.
2. se sim, o WHILE atribui o valor da lista à variável i.
3. o WHILE imprime o valor de i.
4. o WHILE incrementa o valor de x.
5. o WHILE volta ao passo 1.
6. quando x for maior ou igual ao tamanho da lista, o WHILE termina o loop. 

Embora a intrução do FOR seja mais simples, o WHILE é mais flexível, pois permite que você faça qualquer coisa dentro do loop.. 
Normalmente utilizamos o FOR quando sabemos o tamanho da sequência que vamos percorrer e quando quisermos processar os elementos de uma lista, um a um. 
o WHILE é mais indicado quando não sabemos o tamanho da sequência que vamos percorrer e quando quisermos fazer algo mais complexo dentro do loop. ou onde manipulamos o indice de forma NÃO SEQUENCIAL

VALE LEMBRAR: o FOR é mais rápido que o WHILE.

o uso do BREAK tbm interrompe o loop do FOR.
Exemplo3:

L = [1, 2, 3, 4, 5]
p = int(input("Digite um número a pesquisar: "))
for i in L:
    if i == p:
        print('Elemento encontrado')
        break
    else:
        print('Elemento não encontrado')
        
Utiloizamos o BREAK para interromper o loop quando o elemento for encontrado.
"""

# programa 6.6 - Adição de elementos a uma lista

L = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1
    
# Exercício 6.11 Modifique o programa 6.6 usando FOR. Explique por que nem todos os WHILE podem ser transformados em FOR.

L = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)
for x in L:
    print(x)
    
# Resposta: o primeiro while nao pode ser tranformado em for, pois não se sabe o tamanho da lista. Já o segundo while pode ser transformado em for, pois se sabe o tamanho da lista.
