import networkx as nx

class NetworkConverter(object):

    @staticmethod
    def get_network(graph):
        edges_list = []

        for node in graph.nodes:
            for link in node.links:
                edge = (node.id, link.node_link.id, link.weight)
                edges_list.append(edge)
        
        G = nx.Graph()
        G.add_weighted_edges_from(edges_list)

        return G