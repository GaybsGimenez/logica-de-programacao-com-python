"""
Modificar a classe anterior para obter um numero maximo e minimo de canais, senaõ vai até o infinito


"""

from typing import Any


class Televisao:
    def __init__(self, min, max):# para modificar qualquer metodo da classe, é importante adc ele como parametro 
        self.ligada = False
        self.canal = 2 
        self.canal_min = min
        self.canal_max = max
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1 
            
            
            
tv = Televisao(1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
#print(tv.canal) # 99 maximo permitido definido na instancia tv da classe Televisao

for x in range(0,120):
    tv.muda_canal_para_baixo()
print(tv.canal) # 1 minimo permitido definido na instancia tv da classe Televisao


"""
execicio 10.2 
        atualmente a classe Televisao inicia o canal com 2. modifique a classe Televisao de forma a receber o nacal inicial em seu costrutor
        
"""

class Televisao:
    def __init__(self, canal_inicial, min, max):# para modificar qualquer metodo da classe, é importante adc ele como parametro 
        self.ligada = False
        self.canal = canal_inicial
        self.canal_max = max
        self.canal_min = min
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1 
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
            
tv = Televisao(5, 1, 99) # canal_inicla, min, max (tem que seguir a mesma ordem de definição do parametro da classe)
print(tv.canal)
# 5

"""
execicio 10.3
     modificque a classe Televisao de forma que, se pedirmos para mudar o canal para baixo, alem do minimo, ele vá para o canal max.
     e se muda o maximo, ele vá para o min.

"""        

class Televisao:
    def __init__(self, canal_inicial, min, max):# para modificar qualquer metodo da classe, é importante adc ele como parametro 
        self.ligada = False
        self.canal = canal_inicial
        self.canal_max = max
        self.canal_min = min
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1 
        else:
            self.canal = self.canal_max
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1 
        else:
            self.canal = self.canal_min
            
""" 
execicio 10.4 
    modifique o construtor da classe Televisao de forma que min e max sejam parametro opcionais, em que min vale 2 e max 14. 
    caso outro valor nao seja passado
""" 


class Televisao:
    def __init__(self, canal_inicial, min=2, max=14):# para modificar qualquer metodo da classe, é importante adc ele como parametro 
        self.ligada = False
        self.canal = canal_inicial
        self.canal_max = max
        self.canal_min = min
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1 
        else:
            self.canal = self.canal_max
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1 
        else:
            self.canal = self.canal_min
            
"""
execicio 10.5
    na classe Televisao, modifique para criar duas instancias, especificando o valor min e max por nome
    
"""


class Televisao:
    def __init__(self, canal_inicial, min=2, max=14):# para modificar qualquer metodo da classe, é importante adc ele como parametro 
        self.ligada = False
        self.canal = canal_inicial
        self.canal_max = max
        self.canal_min = min
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1 
        else:
            self.canal = self.canal_max
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1 
        else:
            self.canal = self.canal_min

tv = Televisao(2, min=1, max=22) # 2 canal_inicial


tv.muda_canal_para_baixo()
print(tv.canal)
# 1

tv.muda_canal_para_cima()
print(tv.canal)
# 2