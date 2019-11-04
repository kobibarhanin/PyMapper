import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


nodes = set()
edges = []
with open('stack_log.txt', 'r') as stack_log:
    calls = stack_log.read().split(';')
    map_depth = len(calls)-1
    # map_depth = 200
    for call in calls[0:map_depth]:
        lhs, rhs = call.split(',')
        nodes.add(lhs)
        nodes.add(rhs)
        edges.append(call.split(','))


nodes_sizes = [len(node)*250 for node in nodes]
nodes_colors = [idx for idx, node in enumerate(nodes)]


G.add_nodes_from(nodes)
G.add_edges_from(edges)


red_edges = []
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]


pos = nx.kamada_kawai_layout(G)
# pos = nx.bipartite_layout(G,nodes)
# pos = nx.shell_layout(G)
# pos = nx.circular_layout(G)


nx.draw(G, pos, node_color=nodes_colors, node_size=nodes_sizes, edge_color=edge_colors, with_labels=True, cmap=plt.get_cmap('jet'))
plt.show()
