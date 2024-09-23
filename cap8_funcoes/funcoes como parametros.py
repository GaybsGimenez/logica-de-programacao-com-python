"""
python permite a passagem de funções como parâmetros para outras funções.
isso permite combinar várias funções para realizar uma tarefa. 

quando usamos funções como parâmetros, estamos tratando-as como objetos de primeira classe, ou seja,
objetos que podem ser passados como argumentos, retornados por outras funções e atribuídos a variáveis.

"""
# exemplo de uso de funções como parâmetros

def imprime_lista(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)
      
def imprime_elemento(e):
    print(f" valor: {e}")
    
def eh_par(e):
    return e % 2 == 0
def eh_impar(x):
    return not eh_par(x)

L = [1, 7, 9, 2, 3, 4, 5, 6, 8, 10]

imprime_lista(L, imprime_elemento, eh_par)
imprime_lista(L, imprime_elemento, eh_impar)

# retornar a lista de elementos que satisfazem a condição
    