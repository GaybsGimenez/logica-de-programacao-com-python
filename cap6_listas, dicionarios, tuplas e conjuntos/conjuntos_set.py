"""
Conjuntos, SET
- Não possuem valores duplicados
- Não possuem valores ordenados
- Não são acessados via índice, ou seja, não são indexados
Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Conjuntos são estruturas de dados que implementam operações de conjuntos da matemática, como: união, interseção, diferença e diferença simétrica.

um SET() pode ser criado de duas formas:
1 - set()
2 - {}

E pode ser criado apartir de uma lista

b = set([1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5])
b
# retornará {1, 2, 3, 4, 5, 6, 7} 

"""

a = set()
a.add(1)
a.add(2)
a.add(3)

a

# retornará {1, 2, 3}

# Se tentar adcionar um valor que ja existe, não dará erro, mas também não adcionará
a.add(3)
# retornará {1, 2, 3}

# Remover um elemento
a.remove(3)
# retornará {1, 2}

"""
Podemos testar se um elemento está contido no conjunto com o operdaor in

"""

1 in a
# retornará True

-2 in a
# retornará False


# OPERAÇÕES DE CONJUNTOS
# Diferença entre conjuntos

c1 = {0, 1, 2, 3, -1}
c2 = {2,3}
c1 - c2
# retornará {0, 1, -1} ou seja, o resultado contem apenas os elementos do primeiro conjunto que não estão no segundo

# União entre conjuntos
c1 = {0, 1, 2, 3, -1}
c2 = {2,3}
c1 | c2
# retornará {0, 1, 2, 3, -1} ou seja, o resultado contem todos os elementos dos conjuntos que estão unidos
