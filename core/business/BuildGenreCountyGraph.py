from operator import attrgetter
from core.domain.Graph import Graph
from core.domain.Node import Node
from core.domain.Link import Link
from core.domain import Constants

class BuildGenreCountry(object):
   
    def __init__(self, titles):
        self.titles = titles
        self.graph = Graph("Graph for relationship among countries and genres")
        self.distinct_genre = {}
        self.genre_count = 1

    def build_graph(self):
        for title in self.titles:
            links = []
            genres = title.listed_in.split(", ")

            for genre in genres:
                node_link = Node(genre, Constants.GENRE_PREFIX_LABEL)
                node_link.id = self._get_genre_id(genre)
                link = Link(node_link)
                links.append(link)

            #create nodes (countries)
            title_countries = title.country.split(", ")
            for country in title_countries:
                if country:
                    if country.endswith(','):
                        country = country[:-1]

                    new_node = Node(country, Constants.COUNTRY_PREFIX_LABEL)
                    new_node.add_link(links)
                    self.graph.add_node_withid_and_merge_links(new_node)

    def most_common_genre_by_country(self, country_id):
        country_node = next((e for e in self.graph.nodes if e.id == country_id), None)

        if country_node:
            return max(country_node.links, key=attrgetter('weight'))
            
        else:
            return None

    def _get_genre_id(self, genre):
        genre_id = ''
        
        for key in self.distinct_genre:
            if self.distinct_genre[key] == genre:
                genre_id = genre

        if genre_id == '':
            self.distinct_genre[self.genre_count] = genre
            genre_id = genre
            self.genre_count += 1
        
        return '{0}{1}'.format(Constants.GENRE_PREFIX_LABEL, genre_id)
    