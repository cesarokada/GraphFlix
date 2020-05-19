import os.path

from core.domain.Link import Link

class Graph(object):
    def __init__(self, description):
        self.description = description
        self.nodes = []

    def add_node(self, node):
        existent_node = next((e for e in self.nodes if e.description == node.description), None)

        if existent_node != None:
            new_links = Link.merge_links(node.links, existent_node.links)
            existent_node.set_links(new_links)
        else:
            node.id = self._generate_node_id(node.prefix)
            self.nodes.append(node)

    def _generate_node_id(self, prefix):
        generated_id = 1

        if self.nodes:
            last_node = self.nodes[-1]
            number_id = int(last_node.id[1:])
            generated_id = number_id + 1
    
        return '{0}{1}'.format(prefix, generated_id)