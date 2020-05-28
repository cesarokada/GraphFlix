import networkx as nx

class StatisticsNetwork(object):
    
    @staticmethod
    def _get_average_degree(G):
        number_nodes = G.number_of_nodes()
        link_sum = 0

        for node in G.nodes:
            link_sum += G.degree[node]

        return link_sum / number_nodes

    @staticmethod
    def _connected_components_report(G):
        print('Graph is connected: ', nx.is_connected(G))
        print('Number of connected components: ', nx.number_connected_components(G))

        S = [G.subgraph(c).copy() for c in nx.connected_components(G)]

        for i in range(len(S)):
            print(' # {0} Connected components {1}'.format(i + 1, S[i].nodes))

    @staticmethod
    def get_full_report(G):
        print('=====        Statistics Report      ======= ')
        print('Number of Nodes: ', G.number_of_nodes())
        print('Number of Edges: ', G.number_of_edges())
        
        if nx.is_connected(G):
            print('Distance Average: ', nx.average_shortest_path_length(G))
            print('Computed Average Degree: ', StatisticsNetwork._get_average_degree(G))
            print('Clustering Coeficient: ', nx.clustering(G))
        
        StatisticsNetwork._connected_components_report(G)

    