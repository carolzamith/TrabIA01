from Node import Node
from CarregaArquivo import Carrega_arq

__author__ = 'Carol'

filme = Carrega_arq.carrega_arquivo();

kevin_bacon = Node("Kevin Bacon")
# _1 = Node("1")
# _2 = Node("2")
# _3 = Node("3")
# _4 = Node("4")
# _5 = Node("5")
# _6 = Node("6")
# _7 = Node("7")
# _8 = Node("8")
# _10 = Node("10")
#
# _2.set_parent(_1)
# _3.set_parent(_1)
# _4.set_parent(_1)
#
# _5.set_parent(_2)
# _6.set_parent(_2)
#
# _7.set_parent(_4)
# _8.set_parent(_4)
#
# _10.set_parent(_5)
#
# print _1.bfs("11")

# print len(_1.backtrace(_1.bfs("10")))



dict_artista = {}
dict_artista[kevin_bacon.name] = kevin_bacon

# ESTA ERRADO
# for artistas in filme:
#     if artistas[0] == 'Kevin Bacon':
#         artistas.pop(0)
#         last_parent = kevin_bacon
#     else:
#         last_parent = None
#
#
#
#     for artista in artistas:
#         node_artista = dict_artista.get(artista, None)
#
#         if not node_artista:
#             node_artista = Node(artista)
#
#         dict_artista[node_artista.name] = node_artista
#
#         if last_parent:
#             node_artista.set_parent(last_parent)
#
#         last_parent = node_artista
