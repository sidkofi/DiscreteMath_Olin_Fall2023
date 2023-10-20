# visualizing graphs in python

import networkx as nx
import matplotlib.pyplot as plt

# graph definition
graph = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
G = nx.DiGraph()


# add nodes
for x in range(len(graph)):
    G.add_node(x)

# add edges
for i, row in enumerate(graph):
    for j, value in enumerate(row):
        if value == 1:
            G.add_edge(i, j)


layout = nx.spring_layout(G)
# visualize graph
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    layout,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)
plt.title("Directed Unweighted Graph")
plt.show()
