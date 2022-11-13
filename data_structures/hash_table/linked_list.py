class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, node):
        prev_head = self.head
        self.head = node
        node.set_next(prev_head)
    
    def get_head(self):
        return self.head
