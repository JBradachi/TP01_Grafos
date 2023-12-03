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

def recomendacao(G, grafo, arrows=False):
    if numMenu != 1 and numMenu != 10 and numMenu != 14 and numMenu != 20:
        if grafo == 1:
                mostrarGrafo(G)
        else:
            pause = str(input("Pressione enter para prosseguir >>> "))

def visualizarGrafoPrim(G, verticesDesejados, arestasDesejadas, arrows=False):
    pos = nx.spring_layout(G, seed=2500)

    # # Inclui apenas vértices e arestas desejados
    grafoFiltrado = G.subgraph(verticesDesejados + arestasDesejadas)

    # Desenha o grafo
    nx.draw_networkx_nodes(grafoFiltrado, pos, node_size=300)
    nx.draw_networkx_edges(grafoFiltrado, pos, edgelist=arestasDesejadas)

     # Adicionar nome dos vertices
    labels = {v: v for v in verticesDesejados}
    nx.draw_networkx_labels(grafoFiltrado, pos, labels, font_size=10, font_family="sans-serif")
    
    # Adicionar peso
    edge_labels = {(e[0], e[1]): grafoFiltrado[e[0]][e[1]]['weight'] for e in arestasDesejadas}
    nx.draw_networkx_edge_labels(grafoFiltrado, pos, edge_labels=edge_labels)

    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def prim(G):
    
    arvoreMinima = nx.Graph()
    verticeInicial = list(G.nodes())[0]
    visitados = {verticeInicial}
    totalPeso = 0

    while len(visitados) < len(G.nodes()):
        arestasCandidatas = []

        for verticeVisitado in visitados:
            for verticeAdjacente in G.neighbors(verticeVisitado):

                if verticeAdjacente not in visitados:
                    arestasCandidatas.append((verticeVisitado, verticeAdjacente))

        # Seleciona a aresta de menor peso dentre as arestasCandidatas
        menorAresta = min(arestasCandidatas, key=lambda e: G.edges[e]['weight'])

        arvoreMinima.add_edge(menorAresta[0], menorAresta[1], weight=G.edges[menorAresta]['weight'])
        
        totalPeso += G.edges[menorAresta]['weight']

        visitados.add(menorAresta[1])

    print(f"Peso total: {totalPeso}")
    return arvoreMinima
    

def menu():
        limpar_tela()

        """ 
-Determinar a árvore geradora mínima de um grafo.
- A árvore geradora mínima deve ser gerada no formato GraphML e o seu peso
total deve ser retornado.
- Determinar um conjunto estável de vértices de um grafo por meio de uma heurística.
- Determinar o emparelhamento máximo em um grafo.

Faça um programa principal que possibilite testar todas as funcionalidades
"""
        
        print("="*50)
        print("Escolha uma das opções abaixo: \n1 - Mostrar grafo na tela\n2 - Exibir o tamanho do grafo\n3 - Exibir a ordem do grafo")
        print("4 - Determinar grau de um vértice\n5 - Retornar a sequência de graus do grafo\n6 - Determinar a excentricidade de um vertice")
        print("7 - Determinar o raio do grafo\n8 - Determinar o diâmetro do grafo\n9 - Determinar o centro do grafo")
        print("10 - Fazer a busca em largura\n11 - Determinar distância e caminho mínimo\n12 - Determinar centralidade de proximidade de x\n13 - Retornar os vizinhos de um determinado vertice")
        print("14 - Verificar se o grafo possui ciclos\n15 - Encontrar o menor ciclo\n16 - Determinar a árvore geradora mínima\n17 - Determinar um conjunto estável de vértices\n18 - Determinar emparelhamento máximo\n19 - Inserir outro grafo\n20 - Sair do programa")
        numMenu = int(input(">>> "))
        return numMenu

try:
    print("="*100)
    print("Bem vindo ao programa de grafos!\n")
    print("RECOMENDAÇÕES: ")
    print("Deseja que o grafo seja mostrado depois das funcionalidades? O objetivo é facilitar a visualização.\n(1 - sim, 0 - não)")
    print("="*100)
    grafo = int(input(">>> "))
    limpar_tela()
    
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
            
        elif numMenu == 3:
            # Ordem do grafo
            ordem = nx.number_of_nodes(G)
            print(f"Ordem do grafo: {ordem}\n")

        elif numMenu == 4:
            # Grau de um vertice
            vertice = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(vertice not in G.nodes()):
                print("Vertice inválido!\n")
            else:
                grau = G.degree(vertice)
                print(f"Grau do vertice {vertice}: {grau}\n")

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

        elif numMenu == 6: #determinar a excentricidade de um vertice 
            vertice = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(vertice not in G.nodes()):
                print("Vertice inválido!\n")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            if not nx.is_connected(G):
                print("grafo é desconexo")
                continue
            excentricidade = nx.eccentricity(G, vertice, weight="weight")
            print(f"A excentricidade do vértice {vertice} é {excentricidade}")
            
        elif numMenu == 7:
            # Calcular o raio do grafo
            if not nx.is_connected(G):
                print("grafo é desconexo")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            radius = nx.radius(G, weight="weight")

            # Exibir o raio do grafo
            print(f"O raio do grafo é {radius}")

        elif numMenu == 8:
            if not nx.is_connected(G):
                print("grafo é desconexo")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            diametro = nx.diameter(G, weight="weight")
            print(f"O diâmetro do grafo {diametro}")

        elif numMenu == 9:
            if not nx.is_connected(G):
                print("grafo é desconexo")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            centro = nx.center(G, weight="weight")
            print(f"Os nós que compõe o centro do grafo são: ", end="")
            for c in centro:
                print(f"{c}; ", end = "")
            print(end="\n")

        elif numMenu == 10:
            vertice = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(vertice not in G.nodes()):
                print("Vertice inválido!\n")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            tree = nx.bfs_tree(G, vertice)
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

        elif numMenu == 11:
            vertice = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(vertice not in G.nodes()):
                print("Vertice inválido!\n")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            else:
                caminho_min = nx.single_source_dijkstra_path(G, vertice)
                distancia_min = nx.single_source_dijkstra_path_length(G, vertice)
                for v in caminho_min:
                    print(f"\nCaminho mínimo do nó {vertice} até o nó {v}: ", end="")
                    for c in range(len(caminho_min[v]) -1):
                        print(f"{caminho_min[v][c]} ->", end=" ")
                    print(f"{caminho_min[v][-1]}")
                    print(f"Distância mínima do nó {vertice} até o nó {v}: {distancia_min[v]}")

        elif numMenu == 12:
            x = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(x not in G.nodes()):
                print("Vertice inválido!\n")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            else:
                distancia_min = nx.single_source_dijkstra_path_length(G, x)
                soma = 0
                for i in distancia_min:
                    soma += distancia_min[i]
                if (soma == 0):
                    print("A centradidade do vertice {x} é 0")
                    pause = str(input("Pressione enter para prosseguir"))
                    continue
                C = ( nx.number_of_nodes(G)-1)/soma
                print(f"Centralidade do vértice {x} = {C}")

        elif numMenu == 13:
            vertice = str(input(f"Escolha um dos vértices a seguir {G.nodes()} >>>  "))
            if(vertice not in G.nodes()):
                print("Vertice inválido!\n")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            if G.number_of_nodes() == 1:
                print("O grafo contém apenas um vértice")
                pause = str(input("Pressione enter para prosseguir"))
                continue

            print(f"Vizinhos de {vertice}:", end = "")
            for vizinho in G.neighbors(vertice):
                print(f" {vizinho};", end = "")
            print(end = "\n")
            
        elif numMenu == 14:
            temCiclo = len(nx.cycle_basis(G)) > 0 

            if temCiclo:
                print("\nO grafo possui ciclos\nSão eles: ")
                for ciclo in nx.cycle_basis(G):
                    print(ciclo)

            else:
                print("\nO grafo não possui ciclos")
                
            pause = str(input("\nPressione enter para prosseguir"))
            continue
        
        elif numMenu == 15:
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
                print("\nO menor ciclo é o composto pelos nós ", menor_ciclo, " tendo um peso total de ", menor_soma_pesos)
            else: print("\nO grafo não possui ciclos")
            pause = str(input("\nPressione enter para prosseguir"))
            continue
        
        elif numMenu == 16:
            
            if not nx.is_connected(G):
                print("grafo é desconexo")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            
            arvoreMinima = prim(G)
            
            verticesDesejados = list(G.nodes())
            arestasDesejadas = list(arvoreMinima.edges())
            
            visualizarGrafoPrim(G, verticesDesejados, arestasDesejadas)
            # continue
        
        elif numMenu == 17:
            conjEstavel = nx.maximal_independent_set(G)
            print("Possível Conjunto Estável: ")
            print(f"[", end = "")
            for c in range(len(conjEstavel) - 1):
                print(f"{conjEstavel[c]},", end=" ")
            print(f"{conjEstavel[len(conjEstavel)-1]}]")
     
        elif numMenu == 18:
            s = nx.max_weight_matching(G)
            if (len(s) == 0):
                print("O grafo não possui arestas")
                pause = str(input("\nPressione enter para prosseguir"))
                continue
            print("As arestas que fazem parte do emparelhamento máximo são:")
            for i in s:

                print("A aresta " + i[0] + " - " + i[1])    
            
        elif numMenu == 19:
            nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
            nomeDoArquivo =  "./entradas/"+nomeDoArquivo+".graphml"    
            continue
        
        elif numMenu == 20:
            limpar_tela()
            break

        else:
            print("Opção inválida!")
            pause = str(input("Pressione enter para prosseguir"))
        
        recomendacao(G, grafo)
            
except FileNotFoundError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")
except OSError:
    print(f"Erro: O arquivo '{nomeDoArquivo}' não foi encontrado.")