import networkx as nx
import matplotlib.pyplot as plt

INF = 9999999
N = 5
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# Create a graph using NetworkX
G_prim = nx.Graph()

# Create nodes in the graph
G_prim.add_nodes_from(range(N))

edges_to_visualize = []

while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    
    # Add the edge to the list for visualization
    edges_to_visualize.append((a, b, G[a][b]))
    
    selected_node[b] = True
    no_edge += 1

# Visualize the graph
pos = nx.spring_layout(G_prim)
nx.draw(G_prim, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=10)

# Draw the edges with weights
labels = {edge[:2]: edge[2] for edge in edges_to_visualize}
nx.draw_networkx_edge_labels(G_prim, pos, edge_labels=labels)

# Save the plot as an image
plt.savefig("prims_graph.png")

# Close the plot to avoid the warning
plt.close()
