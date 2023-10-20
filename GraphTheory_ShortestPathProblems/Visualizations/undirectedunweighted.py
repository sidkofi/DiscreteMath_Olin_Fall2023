import networkx as nx
import matplotlib.pyplot as plt

# add graph
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]
G = nx.Graph()

# add nodes
for i in range(len(graph)):
    G.add_node(i)

# add edges
for i, row in enumerate(graph):
    for j, value in enumerate(row):
        if i < j and value == 1:
            G.add_edge(i, j)

layout = nx.spring_layout(G)

# draw graph
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    layout,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
)
plt.title("Unweighted Undirected Graph")
plt.show()
