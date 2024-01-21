"""
Se precisar contar as ocorrencias de uma substring em uma string, use o método count().

"""
t = 'um tigre, dois tigres, três tigres'
t.count('tigre')
# 3 pois tigre é substring de tigre|s
t.count('tigres')
# 3 
t.count('t')
# 4 pois t é substring de tigre|s e de três
t.coutn("z")
# 0 pois z não é substring de nada na lista t, ou seja não existe z em t