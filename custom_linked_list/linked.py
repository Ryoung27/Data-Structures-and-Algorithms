class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None:

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        return "[]"

    def add_to_start(self, x):
        pass

    def search_val(self, x):
        pass

    def remove_val_by_index(self, x):
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()
print(my_list)

my_list.append_val(Node(1))
my_list.append_val(Node(2))
my_list.append_val(Node(3))
my_list.append_val(Node(4))
my_list.append_val(Node(5))