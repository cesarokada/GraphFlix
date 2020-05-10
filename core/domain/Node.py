class Node (object):
    
    def __init__(self, description):
        self.id = 0
        self.description = description
        self.links = []

    def add_link(self, links):
        self.links.extend(links)

    def set_links(self, links):
        self.links = links

    def get_formatated_links(self):
        links = ''

        for item in self.links:
            links += "{0} - {1}                         {2} - {3}               weight - {4}\n".format(self.id, self.description, item.node_link.id, item.node_link.description, item.weight)

        return links
