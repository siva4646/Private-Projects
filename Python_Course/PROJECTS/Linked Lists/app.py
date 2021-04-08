class Node:
    def __init__(self, data=None, next=None):
        self.data = data # Any object
        self.next = next # Next Node

class LinkedList:
    def __init__(self):
        self.head = None # First value
    
    def add(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def print_list(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        
        itr = self.head # Iterator, iterates through the Nodes
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        
        print(llstr)

linked_list = LinkedList()
linked_list.add(input("Value: "))
linked_list.add(input("Value: "))
linked_list.add(input("Value: "))
linked_list.print_list()
