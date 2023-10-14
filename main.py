# importando as dependencias
import matplotlib.pyplot as plt
import os 
import networkx as nx

nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
nomeDoArquivo = nomeDoArquivo+".graphml"

# lendo o arquivo hml
G = nx.read_graphml(path=nomeDoArquivo)

def menu():
    os.system('clear')
    print("="*50)
    print("Escolha uma das opções abaixo: \n1 - Mostrar grafo na tela\n2 - Exibir a ordem do grafo\n3 - Exibir o tamanho do grafo")
    print("4 - Determinar grau de um vértice\n5- Retornar a sequência de graus do grafo\n6- Determinar a excentricidade de um vertice")
    print("7 - Determinar o raio do grafo\n8- Determinar o diâmetro do grafo\n9- Determinar o centro do grafo")
    print("10 - Fazer a busca em largura\n11- Determinar distância e caminho mínimo\n12- Determinar centralidade")
    print("13 - Inserir outro grafo\n14 - Sair do programa")
    numMenu = int(input(">>> "))
    return numMenu


while(1):
    
    numMenu = menu()

    if numMenu == 1:
        # mostra grafo na tela bonitinho 
        pos = nx.spring_layout(G, seed=200)
        nx.draw(G, pos)
        plt.show()
        
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
        
    elif numMenu == 13:
        nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
        nomeDoArquivo = nomeDoArquivo+".graphml"
        
        # lendo o arquivo hml
        G = nx.read_graphml(path=nomeDoArquivo)
        
    elif numMenu == 14:
        os.system('clear')
        break
    
    # Função que gera arquivo graphml
    # nx.write_graphml(G, path="<nomeDoArquivo>.graphml")
