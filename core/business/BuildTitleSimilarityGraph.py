from operator import attrgetter
from core.domain.Graph import Graph
from core.domain.Node import Node
from core.domain.Link import Link
from core.domain import Constants

class BuildTitleSimilarityGraph(object):
   
    def __init__(self, titles):
        self.titles = titles
        self.graph = Graph("Graph for relationship titles based on description text")


    def build_graph(self):
        for title in self.titles:
            links = []
            title_node = Node(title.show_id, Constants.TITLE_PREFIX_LABEL, '{0}{1}'.format(Constants.TITLE_PREFIX_LABEL, title.title))
            
            for link_title in self.titles:
                if link_title.show_id == title.show_id:
                    continue

                similarity_coeff = BuildTitleSimilarityGraph._jaccard_similarity_text(title.description, link_title.description)
                
                if Constants.MIN_SIMILARITY_COEFFICIENT <= similarity_coeff:
                    weight = int(similarity_coeff * 100)
                    link_node = Node(link_title.show_id, Constants.TITLE_PREFIX_LABEL, '{0}{1}'.format(Constants.TITLE_PREFIX_LABEL, link_title.title))
                    link = Link(link_node, weight)
                    links.append(link)
            
            title_node.add_link(links)
            self.graph.add_node(title_node)

    def get_most_similar(self, title_id):
        most_similar = next((e for e in self.graph.nodes if e.id == title_id), None)

        if most_similar:
            return max(most_similar.links, key = attrgetter('weight'))
        else:
            return None

    @staticmethod
    def _jaccard_similarity_text(str1, str2):
        a = set(str1.lower().split()) 
        b = set(str2.lower().split())
        c = a.intersection(b)

        return float(len(c)) / (len(a) + len(b) - len(c))

    