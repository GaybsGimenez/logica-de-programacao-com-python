"""  
Strings podem ser tratadas como listas de caracteres. Por exemplo, para obter o primeiro caractere de uma string s, 
você pode escrever s[0]. Strings podem ser indexadas como listas e acessadas como listas, mas não podem ser modificadas como listas.
   
    
"""

# exemplo1: S é uma lista e cada elemento é uma string

S = ['maça', 'banana', 'laranja', 'pera', 'uva', 'manga', 'goiaba', 'abacaxi', 'melancia', 'melão']
len(S)

#retorna o tamanho da lista ou seja a quantidade de elementos S = 10

S[0] #retorna o primeiro elemento da lista S = 'maça'
S[1] #retorna o segundo elemento da lista S = 'banana'
S[2] #retorna o terceiro elemento da lista S = 'laranja' 

#exemplo2: vejamos um programa que lê uma lista de compras até que seja digitado FIM: lendo e imprimindo uma lista de compras

# lista de compras vazia para apendar os produtos
compras = []
# enquanto o usuário não digitar FIM, leia um produto e apende-o na lista de compras
while True:
    # lê um produto
    produto = input('Digite o nome do produto ou FIM para terminar: ')
    # se o produto for FIM, sai do loop e imprime a lista de compras
    if produto == 'FIM':
        break
    compras.append(produto)
    # para cada produto na lista de compras, imprime o produto
    for p in compras:
        print(p)