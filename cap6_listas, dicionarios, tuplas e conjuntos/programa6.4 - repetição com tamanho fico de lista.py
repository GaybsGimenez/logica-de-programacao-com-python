#programa6.4 - repetição com tamanho fico de lista.py
#função len, pode ser usada em repetições para controlar o limite dos índices
 l = [1,2,3]
 x = 0
 while x < 3:
     print(l[x])
     x+=1
#programa6.5 = usando a função len()
 l = [1,2,3]
 x = 0
 while x < len(l): #vantagem, pois se mudarmos a quantidade de elementos da lista, o restante do programa continuará funcionando.
     print(l[x])
     x+=1
