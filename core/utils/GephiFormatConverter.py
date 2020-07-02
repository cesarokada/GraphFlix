import networkx as nx
import os.path

class GephiFormatConverter(object):

    @staticmethod
    def generate_file(G, relative_path, file_name):
        nx.write_gexf(G, os.path.join(relative_path, file_name))