#remoção de elementos da lista del
l = ['a', 'b', 'c']
del l[1]
l
#['a', 'c']

#apagar fatias de uma só vez

l = list(range(101))
del l[1:99)
l
#[0, 99, 100]

#função range gera uma sequencia de elementos, mas um a cada chamada, sendo o que chamamos de generator.
#função list() é utilizada para transformar o resultado dessa função em uma lista. 
