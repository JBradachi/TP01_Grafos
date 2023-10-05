# importando as dependencias
import matplotlib.pyplot as plt
import os 
import networkx as nx

nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
nomeDoArquivo = nomeDoArquivo+".graphml"

# lendo o arquivo hml
G = nx.read_graphml(path=nomeDoArquivo)

while(1):
    os.system('clear')
    print("="*50)
    print("Escolha uma das opções abaixo: \n1 - Mostrar grafo na tela\n2 - Exibir a ordem do grafo\n3 - Exibir o tamanho do grafo\n4 - Inserir outro grafo\n5 - Sair do programa")
    numMenu = int(input(">>> "))

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
        
    elif numMenu == 4:
        nomeDoArquivo = str(input("Insira o nome do arquivo (sem a extensão .graphml) >>> "))
        nomeDoArquivo = nomeDoArquivo+".graphml"
        
        # lendo o arquivo hml
        G = nx.read_graphml(path=nomeDoArquivo)
        
    elif numMenu == 5:
        os.system('clear')
        break


# mostra grafo na tela bonitinho 
#pos = nx.spring_layout(G, seed=200)
#nx.draw(G, pos)
#plt.show()