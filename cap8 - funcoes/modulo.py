"""
depois de criarmos várias funções, os programas poedem ficar muito grandes, precisamos organizar o código. e armazenar as funções 
em arquivos separados é uma boa prática.

todo arquivo .py é um modulo. e todo arquivo .py pode ser importado para outro arquivo .py.

modulos são arquivos que contêm funções e variáveis, e que podem ser importados para outros arquivos.

"""

# exemplo: modulo de entrada (entrada.py) É UM MÓDULO SALVO EM UM ARQUIVO SEPARADO

def valida_inteiro(msg, min, max):
    while True:
        try:
            v = int(input(msg))
            if v >= min and v <= max:
                return v
            else:
                print(f"Digite um valor entre {min} e {max}")
        except ValueError:
            print("Digite um número inteiro")
            
        #.
        #.
        #.
        
        # SUPONDO QUE TENHA OUTRAS FUNÇÕES DENTRO DESSE MESMO MÓDULO
            
            
"""           
# modulo soma (soma.py) que importa o modulo entrada.py

# PARA IMPORTAR UM MÓDULO, USAMOS A PALAVRA RESERVADA import sem o .py
import entrada  # utilizando o import, podemos organizar as funções em um arquivo diferente

L = []

for x in range(10):
    L.append(entrada.valida_inteiro("Digite um número inteiro: ", 0, 20)) # para chamar o método valida_inteiro, precisamos usar o nome do modulo e o nome da função
print(f"Soma: {sum(L)}")    

#chamar modulo = NOMEDOMODULO.NOMEDEFUNCAO


Nem sempre queremos utilizar o nome do módulo para acessar uma função:
    - podemos importar apenas a função que queremos utilizar
    - podemos importar a função com um nome diferente
    
    para importar apenas a função que queremos utilizar, usamos a palavra reservada from
    from NOMEDOMODULO import NOMEDAFUNCAO
    NO NOSSO EXEMPLO:
    from entrada import valida_inteiro # importa apenas a função valida_inteiro do módulo entrada



# exemplo: importar apenas a função que queremos utilizar

from entrada import valida_inteiro

L = []

for x in range(10):
    L.append(valida_inteiro("Digite um número inteiro: ", 0, 20)) 
    

USAR COM ATENÇÃO:

    - se importarmos apenas a função que queremos utilizar, não podemos utilizar as outras funções do módulo
    - se importarmos apenas a função que queremos utilizar, e a função tiver o mesmo nome de uma função que já existe no programa, 
         a função importada irá sobrescrever a função que já existe no programa

"""
