# Pesquisa em uma lista

# definir a função pesquisa que recebe uma lista e um valor e retorna o índice do valor na lista ou None se o valor não existir na lista
def pesquisa (lista, valor):
    # para cada elemento e seu índice na lista
    for indice, elemento in enumerate(lista): # usar enumerate para obter o índice
        # se o elemento for igual ao valor
        if elemento == valor:
            # retornar o índice
            return indice
    # se não encontrar o valor na lista
    return None

L = [10, 20, 25, 30]
print(pesquisa(L, 25))
print(pesquisa(L, 27))

