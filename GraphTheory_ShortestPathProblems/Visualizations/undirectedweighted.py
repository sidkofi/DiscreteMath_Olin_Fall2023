import networkx as nx
import matplotlib.pyplot as plt

# add graph
graph = [
    [0, 2, 1, 4, 0, 3, 0, 0, 0, 1],
    [2, 0, 3, 0, 1, 0, 0, 0, 0, 0],
    [1, 3, 0, 1, 7, 2, 0, 0, 0, 0],
    [4, 0, 1, 0, 2, 5, 0, 0, 0, 0],
    [0, 1, 7, 2, 0, 6, 4, 0, 0, 0],
    [3, 0, 2, 5, 6, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 4, 1, 0, 7, 0, 0],
    [0, 0, 0, 9, 0, 0, 7, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [1, 0, 0, 0, 0, 0, 0, 8, 9, 0],
]
G = nx.Graph()

# add nodes
for i in range(len(graph)):
    G.add_node(i)

# add edges
for i, row in enumerate(graph):
    for j, weight in enumerate(row):
        if i < j and weight > 0:
            G.add_edge(i, j, weight=weight)

layout = nx.spring_layout(G)

# draw grph
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
edge_labels = {(i, j): graph[i][j] for i, j in G.edges()}
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=False,
)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Undirected Weighted Graph")
plt.show()
