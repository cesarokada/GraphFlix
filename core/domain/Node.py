class Node (object):
    
    def __init__(self, description, prefix, id = 0):
        self.id = id
        self.description = description
        self.links = []
        self.prefix = prefix

    def add_link(self, links):
        self.links.extend(links)

    def set_links(self, links):
        self.links = links
