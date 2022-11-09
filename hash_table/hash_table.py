from linked_list import LinkedList
from node import Node
# hash table -> array -> 
#each element is a linked list -> each linked list node has a string
class HashTable:
    def __init__(self, length):
        self.arr = []
        self.length = length
        for i in range(length):
            linked_list = LinkedList()
            self.arr.append(linked_list)
    
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * 263 + ord(c)) % 1000000007
        return ans % self.length

    def add(self, string):
        index = self._hash_func(string)
        linked_list = self.arr[index]
        node = linked_list.head
        while (node != None and node.string != string):
            node = node.next
        if node == None:
            new_node = Node(string)
            linked_list.add_node(new_node)
    




            

