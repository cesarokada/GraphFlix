class Link(object):
    
    def __init__(self, node_link):
        self.weight = 1
        self.node_link = node_link

    @staticmethod
    def merge_links(new_links, current_links):
        all_links = []

        for link in new_links:
            exists_link = False
            
            for link_old in current_links:
                if link_old.node_link.id == link.node_link.id:
                    link_old.weight += 1
                    exists_link = True
                    break

            if not exists_link:
                all_links.append(link)

        all_links.extend(current_links)

        return all_links