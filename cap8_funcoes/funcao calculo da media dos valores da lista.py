# calcular a media dos valores da lista

# definir a função media que recebe uma lista e retorna a media dos valores da lista
def media(lista):
    # inicializar a variavel soma com zero
    soma = 0
    # para cada elemento na lista
    for elemento in lista:
        # somar o elemento na variavel soma
        soma += elemento
    # retornar a soma dividida pelo tamanho da lista    
    return soma / len(lista)


