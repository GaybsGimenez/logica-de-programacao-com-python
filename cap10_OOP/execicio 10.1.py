# Programaçãp orientda a obejtos OOP

"""
É uma tecnica de programaçao que organiza nossos programas em chasses eibjetos em de apenas funções. 

Classe quarda métodos e atributos    
    
    
"""

# exemplo classe televisão

class Televisao: # classes são definidas com a primeira letra maiuscula
    def __init__(self): # __init__ metodo para chamar a classe 
        self.ligada = False # self é um parametro do metodo init. ou seja objeto de televisao
        self.canal = 2 
        
tv = Televisao() # tv recebe uma instancia da classe Televisão/ ou seja, tv se torna obejto da classe Televisao
tv.ligada
# False 

tv.canal
# 2 

# se criar outro objeto 

tv_sala = Televisao() # cria uma nova instancia da classe, chamda tv_sala
tv_sala.ligado = True # redefine os valores padrões definidos anteriormente como True 
tv_sala.canal = 4  # redefine os valores padrões definidos anteriormente como 4 

# agora se chamar tv_sala.ligado, retornará o novo valor associado ao novo objeto da classe

tv_sala.ligado
# True

tv.ligado
# False

"""
Execicio 101 - adc atributos tamanho e marca _a classs Televisao. Crie dois objetos Televisao e atribua tamanhos e marcas diferentes. 
Depois, imprima o valor desses atrbutos de forma a confirmar a independeica dos valores de cada instancia (objetos)       
        
"""

class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal = 2
        self.marca = "LG"
        self.tamanho = 35 
        
tv_new = Televisao()
tv_new.ligada = True
tv_new.canal = 5
tv_new.marca = "Samsung"
tv_new.tamanho = 45 

"""
Como associar um comportamento à classe TELEVISAO. 
DEFININDO 2 METODOS 
muda_canal_para_cima
muda_canal_para_baixo

"""

class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def muda_canal_para_cima(self): # cria-se uma função dentro da classe, essa função vai receber self como parametro
        self.canal += 1 # ai é só definir a logica da função com self
    def muda_canal_para_baixo(self):
        self.canal -= 1
        
tv = Televisao()
tv.muda_canal_para_baixo()
tv.muda_canal_para_cima

tv.canal 
# 4  pois mudou duas vezes para cima 

tv.muda_canal_para_baixo
tv.canal 
# 3 pois muda uma vez para baixo