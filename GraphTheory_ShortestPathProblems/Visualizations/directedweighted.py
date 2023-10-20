import networkx as nx
import matplotlib.pyplot as plt

# add graph
graph = [
    [0, 2, 0, 4, 0, 0, 0, 0, 0, 1],
    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [1, 0, 0, 0, 0, 0, 0, 8, 9, 0],
]
G = nx.DiGraph()

# add nodes
for i in range(len(graph)):
    G.add_node(i)

# add edges and weights
for i, row in enumerate(graph):
    for j, value in enumerate(row):
        if value != 0:
            G.add_edge(i, j, weight=value)

layout = nx.spring_layout(G)

# draw graph
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
    arrows=True,
)

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Directed Weighted Graph")
plt.show()
