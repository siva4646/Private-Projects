class Node:
    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = nextval

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
# list.headval = Node("Intel")
n = ''
try:
    n = int(input("How many nodes? "))
except ValueError:
    print('Please use integer values!')
    exit()

    
for i in range(0, n):
    if i == 0:
        list.headval = Node(input("Node: "))
    else:
        list.AtEnd(input("Node: "))

list.listprint()

