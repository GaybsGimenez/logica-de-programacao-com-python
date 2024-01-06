#metodo extende() e append()

l = ["a"]
#['a']
l.append("b")
l
#['a', 'b']

l.extend("c")
l
#['a', 'b', 'c']

#quando adc apenas elementos, tanto append, quando l + [1] produzem o mesmo resultado
#isso ocorre porque, quando adc uma lisa a outra, o interpretador excuta um método chamado EXTENDE(), que adc os elementos de uma lista em outra.

l.append(['d', 'e'])
l
#['a', 'b', 'c', ['d', 'e']]

l.extend(['f', 'g', 'h'])
l
#['a', 'b', 'c', ['d', 'e'], 'f', 'g', 'h']

#APPEND adiciou a uma lista dentro da lista l - se usar o métodos append como uma lista de parâmetro, em vez de adc os elementos no fim da lista, append adc, na vdd, a lista inteira. PORÉM, COMO APENAS UM NOVO LEMENTO
#EXTENDE adicionou os elementos à lista l - exetend não aceita outros parâmetros, somente LISTAS.

len(l)
#7 - ['a', 'b', 'c', ['d', 'e'], 'f', 'g', 'h']
#      1    2    3        4       5    6    7
