class Node:
  def __init__(self, data):
    self.data = 0
    self.next = None

class List:
  def __init__(self):
    self.head = None

# Creating various nodes
a = Node(2)
b = Node(3)
c = Node(4)

a.next = b
b.next = c

# Creating the list
l = List()
l.head = a

# To pass a list in fun, one can pass "l"
