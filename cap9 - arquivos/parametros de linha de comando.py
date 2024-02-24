"""
modulo sys é utilizado para acessar os argumentos passados na linha de comando, ou seja, 
os parametros passados quando executamos um programa no terminal

Podemos acessar os parâmetros passados ao programa na linha de comando utilizando o módulo sys e trabalhado com a lista argv.


"""

# exemplo

# importar o modulo sys que é utilizado para acessar os argumentos passados na linha de comando, é util quando 
# queremos passar parametros para o programa
import sys
# imprime o nome do programa, leia o primeiro parametro da lista sys.argv
print("Numero de parametros: ", len(sys.argv))
print("Lista de parametros: ", str(sys.argv))

# para cada parametro na lista sys.argv imprima o numero do parametro e o parametro
for n, p in enumerate(sys.argv):
    print(f"Parametro {n} = {p}")
    
# para chamar o script na linha de comando

# fparam.py primeiro segundo terceiro
# fparam.py 1 2 3
# 