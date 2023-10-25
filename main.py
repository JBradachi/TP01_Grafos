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
    pos = nx.spring_layout(G, seed=500)  # positions for all nodes - seed for reproducibility

    # vertice
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # aresta
    if (arrows == True):
        nx.draw_networkx_edges(G, pos, width=6, arrowstyle="->", arrowsize=40)
    else:
        nx.draw_networkx_edges(G, pos, width=6)

    # vertice labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    pesos = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, pesos)

    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def menu():
        limpar_tela()
        
        print("="*50)
        print("Escolha uma das opções abaixo: \n1 - Mostrar grafo na tela\n2 - Exibir o tamanho do grafo\n3 - Exibir a ordem do grafo")
        print("4 - Determinar grau de um vértice\n5 - Retornar a sequência de graus do grafo\n6 - Determinar a excentricidade de um vertice")
        print("7 - Determinar o raio do grafo\n8 - Determinar o diâmetro do grafo\n9 - Determinar o centro do grafo")
        print("10 - Fazer a busca em largura\n11 - Determinar distância e caminho mínimo\n12 - Determinar centralidade\n13 - Retornar os vizinhos de um determinado vertice")
        print("14 - Inserir outro grafo\n15 - Sair do programa")
        numMenu = int(input(">>> "))
        return numMenu

try:

   
    nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
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

        numMenu = menu()

        if numMenu == 1:
            # mostra grafo na tela 
            mostrarGrafo(G)
            
        elif numMenu == 2:
            # Tamanho do grafo
            tamanho = nx.number_of_edges(G)
            print(f"Tamanho do grafo: {tamanho}\n")
            pause = str(input("Pressione enter para prosseguir"))
            
        elif numMenu == 3:
            # Ordem do grafo
            ordem = nx.number_of_nodes(G)
            print(f"Ordem do grafo: {ordem}\n")
            pause = str(input("Pressione enter para prosseguir"))

        elif numMenu == 4:
            # Grau de um vertice
            vertice = str(input(f"Insira o numero do vertice [0 até {nx.number_of_nodes(G)-1}] >>>  "))
            if(int(vertice) > nx.number_of_nodes(G)-1 or int(vertice) < 0):
                print("Vertice inválido!\n")
            else:
                grau = G.degree(vertice)
                print(f"Grau do vertice {vertice}: {grau}\n")
            pause = str(input("Pressione enter para prosseguir"))

        elif numMenu == 5:
            # Sequencia de graus do grafo
            graus = G.degree()
            print(f"Sequencia de graus do grafo:")
            somenteGraus = []
            for g in graus:
                somenteGraus.append(g[1])
                print(f"Grau do vertice {g[0]}: {g[1]}")
            print(f"Na notacao comum: d = [", end = "")
            somenteGraus.sort(reverse=True)
            for c in range(len(somenteGraus) - 1):
                print(f"{somenteGraus[c]},", end=" ")
            print(f"{somenteGraus[len(somenteGraus)-1]}]")
            pause = str(input("\nPressione enter para prosseguir"))

        elif numMenu == 6: #determinar a excentricidade de um vertice 
            vertex = str(input(f"Insira o numero do vertice [0 até {nx.number_of_nodes(G)-1}] >>>  "))
            if (int(vertex) >= nx.number_of_nodes(G) or int(vertex) < 0):
                print("Vertice invalido!!")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            excentricidade = nx.eccentricity(G, vertex, weight="weight")
            print(f"A excentricidade do vértice {vertex} é {excentricidade}")
            pause = str(input("\nPressione enter para prosseguir"))
            
        elif numMenu == 7:
            # Calcular o raio do grafo
            radius = nx.radius(G, weight="weight")

            # Exibir o raio do grafo
            print(f"O raio do grafo é {radius}")
            pause = str(input("\nPressione enter para prosseguir"))

        elif numMenu == 8:
            diametro = nx.diameter(G, weight="weight")
            print(f"O diâmetro do grafo {diametro}")
            pause = str(input("Pressione enter para prosseguir"))

        elif numMenu == 9:
            centro = nx.center(G, weight="weight")
            print(f"Os nós que compõe o centro do grafo são ", end="")
            for c in centro:
                print(f"{c}; ", end = "")
            print(end="\n")
            pause = str(input("Pressione enter para prosseguir"))

        elif numMenu == 10:
            print(f"Digite o vertice raiz da arvore (entre 0 e {nx.number_of_nodes(G)-1}) >>> ", end = "")
            source = str(input())
            if (int(source) >= nx.number_of_nodes(G) or int(source) < 0):
                print("Vertice inválido!!")
                pause = str(input("Pressione enter para prosseguir"))
                continue
            tree = nx.bfs_tree(G, source)
            print("Arestas que nao fazem parte da arvore: ", end = "")
            count = 1
            for edge in G.edges():
                achou = 0
                for edge2 in tree.edges():
                    v = [edge[0],edge[1]]
                    v2 = [edge2[0],edge2[1]]
                    v.sort()
                    v2.sort()
                    if (v[0] == v2[0] and v[1] == v2[1]):
                        achou = 1
                        break
                if not achou:
                    count = 0
                    print(f" [{edge[0]}, {edge[1]}];", end = "")


            if count:
                print ("Todos as arestas fazem parte da arvore")
            nx.set_edge_attributes(tree, G.edges())
            mostrarGrafo(tree, arrows=True)
            nx.write_graphml_xml(tree, "./entradas/saidas/saida.graphml")
            pause = str(input("\nPressione enter para prosseguir"))

        elif numMenu == 11:
            # Determinar distância e caminho minimo
            vertice = str(input(f"Insira o nó de origem [0 até {nx.number_of_nodes(G)-1}] >>>  "))
            if(int(vertice) > nx.number_of_nodes(G)-1 or int(vertice) < 0):
                print("Vertice inválido!\n")
            else:
                caminho_min = nx.single_source_dijkstra_path(G, vertice)
                distancia_min = nx.single_source_dijkstra_path_length(G, vertice)
                for v in caminho_min:
                    print(f"\nCaminho mínimo do nó {vertice} até o nó {v}: ", end="")
                    for c in range(len(caminho_min[v]) -1):
                        print(f"{caminho_min[v][c]} ->", end=" ")
                    print(f"{caminho_min[v][-1]}")
                    print(f"Distância mínima do nó {vertice} até o nó {v}: {distancia_min[v]}")

            pause = str(input("\nPressione enter para prosseguir"))
        elif numMenu == 12:
            centro = nx.center(G)
            print("Os vertices do centro são: ", end=' ')
            for a in centro:
                print(a, end = "; ")
            print('\n')
            pause = str(input("Pressione enter para prosseguir"))

        elif numMenu == 13:
            vertice = str(input(f"Insira o nó de origem [0 até {nx.number_of_nodes(G)-1}] >>>  "))
            if G.number_of_nodes() == 1:
                print("O grafo contém apenas um vértice")
                pause = str(input("Pressione enter para prosseguir"))
                continue

            print(f"Vizinhos de {vertice}:", end = "")
            for vizinho in G.neighbors(vertice):
                print(f" {vizinho};", end = "")
            print(end = "\n")
            pause = str(input("Pressione enter para prosseguir"))
            continue
        elif numMenu == 14:
            nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
            nomeDoArquivo =  "./entradas/"+nomeDoArquivo+".graphml"    
            continue
            
        elif numMenu == 15:
            limpar_tela()
            break

        else:
            print("Opção inválida!")
            pause = str(input("Pressione enter para prosseguir"))
        
            
except FileNotFoundError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")
except OSError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")