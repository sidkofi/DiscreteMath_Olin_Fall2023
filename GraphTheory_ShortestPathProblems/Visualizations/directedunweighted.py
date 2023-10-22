# visualizing graphs in python

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

GRAPH_TYPE = "Directed Unweighted Graph"
# graph definition
graph = [
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
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


pos = nx.spring_layout(G)
# visualize graph
plt.figure(figsize=(8, 8))
nx.draw_networkx(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)

filename = f"GraphTheory_ShortestPathProblems/Visualizations/assets/{GRAPH_TYPE.replace(' ', '_')}.png"
path = nx.shortest_path(G, source=0, target=9)
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="r")
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=2)
plt.title(GRAPH_TYPE)
legend_elements = [Line2D([0], [0], color="red", lw=4, label="Shortest Path")]
plt.legend(handles=legend_elements, loc="upper right")
plt.savefig(filename)
plt.show()
