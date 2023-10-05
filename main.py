# importando as dependencias
import matplotlib.pyplot as plt
import networkx as nx

# lendo o arquivo hml
G = nx.read_graphml(path="grafoTeste2.graphml")

# Ordem do grafo
ordem = nx.number_of_nodes(G)
print(f"Ordem do grafo: {ordem}\n")


# Tamanho do grafo
tamanho = nx.number_of_edges(G)
print(f"Tamanho do grafo: {tamanho}\n")


# mostra grafo na tela bonitinho 
#pos = nx.spring_layout(G, seed=200)
#nx.draw(G, pos)
#plt.show()