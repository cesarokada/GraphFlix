class Node (object):
    
    def __init__(self, description):
        self.id = 0
        self.description = description
        self.links = []

    def add_link(self, links):
        self.links.extend(links)

    def get_formatated_links(self):
        links = ''

        for item in self.links:
            links += "{0} - {1}                         {2} - {3}\n".format(self.id, self.description, item.id, item.description)

        return links
