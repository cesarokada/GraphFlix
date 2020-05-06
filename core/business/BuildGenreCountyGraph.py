from core.domain.Graph import Graph
from core.domain.Node import Node

class BuildGenreCountry(object):
   
    def __init__(self, titles):
        self.titles = titles
        self.graph = Graph("Graph for relationship among countries and genres")
        self.distinct_genre = {}
        self.genre_count = 1

    def build_graph(self):
        for title in self.titles:
            #create links (genres)
            links = []
            genres = title.listed_in.split(", ")

            for genre in genres:
                new_link = Node(genre)
                new_link.id = self._get_genre_id(genre)
                links.append(new_link)

            #create nodes (countries)
            title_countries = title.country.split(", ")

            for country in title_countries:
                new_node = Node(country)
                new_node.add_link(links)
                self.graph.add_node(new_node)

    def _get_genre_id(self, genre):
        genre_id = 0
        
        for key in self.distinct_genre:
            if self.distinct_genre[key] == genre:
                genre_id = key

        if genre_id == 0:
            self.distinct_genre[self.genre_count] = genre
            genre_id = self.genre_count
            self.genre_count += 1
        
        return genre_id
        

    