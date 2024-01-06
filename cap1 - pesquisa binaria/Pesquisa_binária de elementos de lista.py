#Pesquisa_binária de elementos de lista

lista = [1, 3, 5, 7, 9]
def pesquisa_binaria(lista, item)
baixo = 0
alto = len(lista) - 1

while baixo <= alto:
    meio = (baixo + alto)/2
    chute = lista[meio]
    if chute == item:
        retorn meio
    if chute > item:
        alto = meio - 1
    else:
        baixo = meio + 1
return None

print pesquisa_binaria(minha_lista, 3)
print pesquisa_binaria(minha_lista, -1)
