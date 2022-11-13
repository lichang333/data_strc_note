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

    def search(self, string, linked_list):
        node = linked_list.head
        # while (node != None and node.string != string):
        while (node and node.string != string):
            node = node.next
        return node

    def lookup(self, string):
        index = self._hash_func(string)
        # linked_list = self.arr[index]
        # return linked_list
        return self.arr[index]

    def add(self, string):
        linked_list = self.lookup(string)
        node = self.search(string, linked_list)
        if node == None:
            new_node = Node(string)
            linked_list.add_node(new_node)
    
    def find(self, string):
        linked_list = self.lookup(string)
        return self.search(string, linked_list)
        # if node == None:
        #     return False
        # else:
        #     return True
        
    def delete(self, string):
        linked_list = self.lookup(string)
        node = linked_list.head
        while (node and node.next and node.next.string != string):
            node = node.next
            
        # if node == None or node.next == None:
        #     return
        # else:
            # node.next = node.next.next
        # if node != None and node.next != None:
        if node and node.next:
            node.set_next(node.next.next)
            
    def check(self, index):
        # index = self._hash_func(string)
        linked_list = self.arr[index]
        # return linked_list
        # return self.arr[index]
        node = linked_list.head
        string = ""
        while node:
            string += node.string
            node = node.next
        return string
            


            



            

