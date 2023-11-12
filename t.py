# importando as dependencias
import matplotlib.pyplot as plt
import os 
import networkx as nx
# biblioteca para ler peso dos arquivo graphml
import xml.etree.ElementTree as ET

def limpar_tela():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')
        
def mostrarGrafo(G, arrows=False):
    pos = nx.spring_layout(G, seed=2500)  # positions for all nodes - seed for reproducibility

    # vertice
    nx.draw_networkx_nodes(G, pos, node_size=300)

    # aresta
    if (arrows == True):
        nx.draw_networkx_edges(G, pos, width=5, arrowstyle="->", arrowsize=20)
    else:
        nx.draw_networkx_edges(G, pos, width=5, node_size=200)

    # vertice labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    pesos = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, pesos)

    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def menu():
        limpar_tela()


try:
    limpar_tela()
    
    nomeDoArquivo = "gCiclos"
    nomeDoArquivo =  "./entradas/"+nomeDoArquivo+".graphml"    
    
    

    while(1):
        # lendo o arquivo hml
        limpar_tela()

        # Ler o arquivo GraphML
        tree = ET.parse(nomeDoArquivo)
        root = tree.getroot()

        # Crie um objeto Graph (grafo não direcionado) com o NetworkX
        G = nx.Graph()

        # Itere sobre as arestas no arquivo XML e adicione-as ao grafo NetworkX com seus pesos
        for edge in root.findall(".//edge"):
            source = edge.get('source')
            target = edge.get('target')
            weight = float(edge.get('weight'))
            G.add_edge(source, target, weight=weight)
        
        # 14
        temCiclo = len(nx.cycle_basis(G)) > 0 

        if temCiclo:
            print("O grafo possui ciclos")
        else:
            print("O grafo não possui ciclos")

        print()
        # elif numMenu == 15:
        if(len(nx.cycle_basis(G)) > 0):
            ciclos = nx.cycle_basis(G)
            # menor_soma recebe infinito para primeira comparação
            menor_soma_pesos = float("inf")

            for ciclo in ciclos:
                soma_pesos = 0
                for i in range(len(ciclo)):
                    vertice_atual = ciclo[i]
                    proximo_vertice = ciclo[(i + 1) % len(ciclo)]

                    # pega as informações da aresta entre o vertice atual e o proximo vertice
                    dados_aresta = G.get_edge_data(vertice_atual, proximo_vertice)

                    peso_aresta = dados_aresta['weight']

                    # Adiciona o peso ao total
                    soma_pesos += peso_aresta

                if soma_pesos < menor_soma_pesos:
                    menor_soma_pesos = soma_pesos
                    menor_ciclo = ciclo
        print("O menor ciclo é o composto pelos nós ", menor_ciclo, " tendo um peso total de ", menor_soma_pesos)
        break
    else: print("O grafo não possui ciclos")
            


        
except FileNotFoundError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")
except OSError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")