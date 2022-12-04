import matplotlib.pyplot as plt
import networkx as nx

def drawGraph(G):
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def loadListOfMatrixEdges(file):
    G = nx.Graph()
    with open(f'{file}', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            els = line.split(' ')
            if(els[2][-1]=='\n'):
                els[2] = els[2][:-1]
                weight1 = float(els[2])
            G.add_edge(els[0], els[1], weight=weight1)
    return G

def loadAdjacencyMatrix(file):
    G = nx.Graph()
    currLineIndex = 0
    with open(f'{file}', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            els = line.split(' ')
            size_of_matrix = len(els)

            if (els[size_of_matrix-1][-1] == '\n'):
                els[size_of_matrix-1] = els[size_of_matrix-1][:-1]

            for i in range(currLineIndex+1, size_of_matrix):
                weight1 = float(els[i])
                if(weight1):
                    G.add_edge(i, currLineIndex, weight=weight1)
            currLineIndex+=1
    return G

def check_3rd_task(G):
    if (G.number_of_nodes() > 3):
        edlist = []
        for i in range(1, G.number_of_edges()):
            if (int(str(G.degree([f'{i}'])).split(' ')[1][:-2]) == 3):
                # print(str(G.degree([f'{i}'])).split(' ')[0][3:-2])
                edlist.append(str(G.degree([f'{i}'])).split(' ')[0][3:-2])
        for i in range(0, len(edlist) - 1):
            for j in range(i, len(edlist)):
                if (G.has_edge(edlist[i], edlist[j])):
                    return True
    return False

if __name__ == '__main__':

    # 1
    # G = nx.Graph()
    # drawGraph(G)

    # G = nx.Graph()
    # G.add_edge("1", "2", weight=0.6)
    # G.add_edge("1", "3", weight=0.2)
    # G.add_edge("3", "d", weight=0.1)
    # G.add_edge("3", "5", weight=0.7)
    # G.add_edge("3", "6", weight=0.9)
    # G.add_edge("1", "4", weight=0.3)
    # drawGraph(G)

    # 2a
    # G = loadListOfMatrixEdges('1.txt')
    # drawGraph(G)

    # 2b
    # G = loadAdjacencyMatrix('2.txt')
    # drawGraph(G)

    G = loadListOfMatrixEdges('1.txt')
    print(check_3rd_task(G))

