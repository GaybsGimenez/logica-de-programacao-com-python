"""
Uma variável local é uma variável que é declarada dentro de uma função. Ela só pode ser usada dentro da função onde foi declarada.
uma variável global é uma variável que é declarada fora de uma função. Ela pode ser usada em qualquer lugar do programa.

"""

# exemplo de variável global

EMPRESA = "Google"

def imprime_empresa():
    print(EMPRESA)
    print("-" * len(EMPRESA))
    
# a função imprime_empresa() pode não recebe parâmetros nem retorna valores, ela simplesmente imprime o nome da empres e traço abaixo dele

# a variável EMPRESA é uma variável global, pois foi declarada fora de qualquer função.

"""
um bom uso de variáveis globais é para guardar valores constantes e que devem ser acessados por várias funções do programa.


IMPORTANTE: devido a capacidade do python de declarar variáveis a medida que usamos, é possível que uma variável local tenha o mesmo nome de uma variável global. Nesse caso, a variável local tem prioridade sobre a variável global.
"""

# exemplo: 
a =5 # criamos a variável global
def mudar_e_imprimte(): # definimos a função para mudar e imprimir a variável
    a = 7 # definimos a variável local
    print(f"a variável A dentro da função é: {a}") # imprimimos a variável local, dentro da função pois ela não altera, antes de passar pela função.

print(f"a variável A fora da função é: {a}") # imprimimos a variável global, antes de passar pela função. 

mudar_e_imprimte() # chamamos a função para mudar o valor da variável e imprimi-la
print(f"a variável a depois de passar pela função muda_e_imprime é: {a}") # imprimimos a variável global, depois de passar pela função. agora esse é o valor da variável global.

