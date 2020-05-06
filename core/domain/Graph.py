class Graph(object):
    def __init__(self, description):
        self.description = description
        self.nodes = []

    def add_node(self, node):
        existent_node = next((e for e in self.nodes if e.description == node.description), None)

        if existent_node != None:
            new_links = self._get_difference_among_links(node.links, existent_node.links)
            existent_node.add_link(new_links)
        else:
            node.id = self._generate_node_id()
            self.nodes.append(node)

    def print_graph(self):
        for node in self.nodes:
            print(node.get_formatated_links())

    def _generate_node_id(self):
        generated_id = 1

        if self.nodes:
            last_node = self.nodes[-1]
            generated_id = last_node.id + 1
    
        return generated_id

    def _get_difference_among_links(self, new_links, recent_links):
        diff_links = []

        for link in new_links:
            exists = False
            
            for link_old in recent_links:
                if link_old.id == link.id:
                    exists = True
                    break

            if not exists:
               diff_links.append(link) 

        return diff_links