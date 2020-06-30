import networkx as nx
import os.path

class GephiFormatConverter(object):

    @staticmethod
    def generate_file(G, relative_path, file_name):
        nodes = []
    
        with open(os.path.join(relative_path, file_name), "w") as file:
            file.write('*Vertices {0}'.format(G.number_of_nodes()))
            
            for node in G.nodes:
                nodes.append(node)
                file.write('\n{0} "{1}"'.format(nodes.index(node) + 1, node))

            file.write('\n*Edges')
            for edge in G.edges.data('weight', default = 1):
                file.write('\n{0} {1} {2}'.format(nodes.index(edge[0]) + 1, nodes.index(edge[1]) + 1, edge[2]))