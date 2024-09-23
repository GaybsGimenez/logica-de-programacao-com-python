"""
Diconários são similares a listas, mas com relação de chave e valor

Um dicionário é acessado por sua chave

Diferente de listas, em que o indice é uma numero, os dicionarios utilizam chave como indice

Quando atribuimos um valor a uma chave duas coisas podem acontecer:

1 - se a chave ja existir, o valor associado é alterado para o novo valor
2 - se a chave nao existir, a nova chave será criada no dicionario

LEMBRANDO QUE: um dicionario não pode haver duas ou mais chaves de mesmo nome, mas pode haver duas ou mais valores com o mesmo nome/valor

um dicionario é definido por {chave: valor, chave: valor, chave: valor}

"""

# Observe:

tabela = {
    "alface": 0.45,
    "batata": 0.70,
    "tomate": 2.30,
    "feijão": 1.00    
}

print(tabela["tomate"])

# retornará 2.30 pois, printamos o valor associado à chave 'tomate' da variavel tabela. 

# para SUBSTITUIR um valor associado a uma tabela, entramos com a variavel tabela, na "coluna"/ chave tomate e igualamos ao novo valor
tabela["tomate"] = 3.00

# para adicionar um novo valor ao dicionario da variavel tabela é o mesmo processo, mas com um nova chave
tabela["cebola"] = 4.00

# quanto o acesso ao dado, deve-se verificar se uma chave existe antes de acessa-la
print(tabela["manga"])
# gera um erro: keyError: 'manga'

# para ver se existe a chave usar "in" printa, a chave desejada em/na (in) tabela
print("manga" in tabela)
# False


# Podemos ter uma lsita com as chaves ou valores
print(tabela.keys())
# retorna dict_keys([todas as chaves])

print(tabela.values())
# retorna dict_keys([todos os valores])


# exemplo1: obtenção do preço com um dicionário
tabela = {
    "alface": 0.45,
    "batata": 0.70,
    "tomate": 2.30,
    "feijão": 1.00    
}

while True:
    produto = ("Digite o nome do produto ou 'fim' para terminar: ")
    if produto == "fim": 
        break
    if produto in tabela:
        print(f"preço {tabela[produto]:5.2f}")
    else:
        print("produto não encontrado")

"""
Diconário com listas. 
podemos ter dicionarios com listas, tuplas, outros dicionarios, etc associados a uma chave.

   
"""

#exemplo: um estoque de mercadoria que além dos preços associado ao produto, também tivesse a quantidade em estoque 
tabela = {
    "alface": [1000, 0.45],  # lembrando que o primeiro valor é a quantidade e o segundo o preço
    "batata": [500, 0.70],
    "tomate": [2000, 2.30],
    "feijão": [100, 1.00]    
}

# venda é uma variavel que recebe uma lista de listas, onde cada lista interna tem o nome do produto e a quantidade vendida
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
# total é uma variavel que recebe o valor total da venda inicialmente 0
total = 0 
print("Vendas:\n")

# para cada operação na lista venda, onde operação é uma lista com o nome do produto e a quantidade vendida
for operação in venda:
    # produto recebe o nome do produto
    produto, quantidade = operação 
    # preço recebe o preço do produto
    preço = tabela[produto][1]
    # custo recebe o preço do produto vezes a quantidade vendida
    custo = preço * quantidade
    
    # printa o nome do produto, a quantidade vendida, o preço do produto e o custo da venda
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    # tabela[produto][0] é a quantidade em estoque do produto, e -= quantidade é a quantidade em estoque menos a quantidade vendida
    tabela[produto][0] -= quantidade
    # total recebe o total mais o custo.
    # += é o mesmo que total = total + custo
    total += custo

print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in tabela.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
    