import networkx as nx

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("B", "C"), ("C", "D"), ("A", "D")])

print(G.nodes())  
print(G.edges()) 
 
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000)
plt.show()
