import networkx as nx
import matplotlib.pyplot as plt

nodes = set()
edges = []
with open('/Users/kobarhan/workspace/PyMapper/Targets/simpleApp/stack_log.txt', 'r') as stack_log:
    calls = stack_log.read().split(';')

    for call in calls[:-1]:
        lhs, rhs = call.split(',')
        nodes.add(lhs)
        nodes.add(rhs)
        edges.append(call.split(','))


nodes_sizes = [len(node)*250 for node in nodes]
nodes_colors = [idx for idx, node in enumerate(nodes)]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.draw(G, cmap=plt.get_cmap('jet'),
        with_labels=True,
        node_shape='o' ,
        node_size=nodes_sizes,
        node_color=nodes_colors)

plt.show()
