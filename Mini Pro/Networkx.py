import networkx as nx
import matplotlib.pyplot as plt

# Directed graph
DG = nx.DiGraph()
DG.add_edge("A", "B")
DG.add_edge("B", "C")
DG.add_edge("C", "A")

# Weighted graph
WG = nx.Graph()
WG.add_edge("X", "Y", weight=5)
WG.add_edge("Y", "Z", weight=3)

print(WG.edges(data=True))  # see weights
nx.draw(DG)
plt.show()