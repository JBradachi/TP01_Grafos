import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_graphml(path="grafoTeste.graphml")

pos = nx.spring_layout(G, seed=200)
nx.draw(G, pos)
plt.show()