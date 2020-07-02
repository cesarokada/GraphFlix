import networkx as nx

class NetworkConverter(object):

    @staticmethod
    def get_network(graph):
        edges_list = []
        G = nx.Graph()

        for node in graph.nodes:
            G.add_node(node.id)   
            
            for link in node.links:
                edge = (node.id, link.node_link.id, link.weight)
                edges_list.append(edge)
        
       
        G.add_weighted_edges_from(edges_list)

        return G