import operator
import networkx as nx
from networkx.algorithms import community

class StatisticsNetwork(object):
    
    @staticmethod
    def _connected_components_report(G):
        print('---- Component Report -----')
        is_connected = nx.is_connected(G)
        components = nx.connected_components(G)

        print("Network is connected: ", is_connected)
        print('Number of connected components: ', nx.number_connected_components(G))

        largest_component = largest_component = max(components, key=len)
        subgraph = G.subgraph(largest_component)
        diameter = nx.diameter(subgraph)
        print("Network diameter of largest component:", diameter)

    @staticmethod
    def _centrality_metrics(G):
        print('---- Centrality Report -----')
        degree_dict = dict(G.degree(G.nodes()))
        nx.set_node_attributes(G, degree_dict, 'degree')
        sorted_degree = sorted(degree_dict.items(), key=operator.itemgetter(1), reverse=True)
        
        print("Top 20 nodes by degree:")
        for d in sorted_degree[:20]:
            print(d)

        betweenness_dict = nx.betweenness_centrality(G) # Run betweenness centrality
        eigenvector_dict = nx.eigenvector_centrality_numpy(G) # Run eigenvector centrality

        # Assign each to an attribute in your network
        nx.set_node_attributes(G, betweenness_dict, 'betweenness')
        nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')

        sorted_betweenness = sorted(betweenness_dict.items(), key=operator.itemgetter(1), reverse=True)

        print("Top 20 nodes by betweenness centrality:")
        for b in sorted_betweenness[:20]:
            print(b)

    @staticmethod
    def get_community_report(G):
        print('---- Community Report -----')
        communities = community.greedy_modularity_communities(G)
        
        modularity_dict = {} # Create a blank dictionary
        for i,c in enumerate(communities): # Loop through the list of communities, keeping track of the number for the community
            for name in c: # Loop through each person in a community
                modularity_dict[name] = i # Create an entry in the dictionary for the person, where the value is which group they belong to.

        # Now you can add modularity information like we did the other metrics
        nx.set_node_attributes(G, modularity_dict, 'modularity')
        
        # First get a list of just the nodes in that class
        class0 = [n for n in G.nodes() if G.nodes[n]['modularity'] == 0]

        # Then create a dictionary of the eigenvector centralities of those nodes
        class0_eigenvector = {n:G.nodes[n]['eigenvector'] for n in class0}

        # Then sort that dictionary and print the first 5 results
        class0_sorted_by_eigenvector = sorted(class0_eigenvector.items(), key=operator.itemgetter(1), reverse=True)

        print("Modularity Class 0 Sorted by Eigenvector Centrality:")
        for node in class0_sorted_by_eigenvector[:5]:
            print("Name:", node[0], "| Eigenvector Centrality:", node[1])

    @staticmethod
    def _get_basic_report(G):
        print(nx.info(G))
        print("Network density:", nx.density(G))

    @staticmethod
    def get_full_report(G):
        print('=====        Statistics Report      ======= ')
        StatisticsNetwork._get_basic_report(G)
        StatisticsNetwork._connected_components_report(G)
        StatisticsNetwork._centrality_metrics(G)
        StatisticsNetwork.get_community_report(G)
        

    