# Monday

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

class Linked_list:
  def __init__(self, head, tail):
    self.head = head
    self.tail = tail
    self.length = 0

    def add_to_tail(self, value):
      n = Node(value)
      self.tail.next_node = n
      self.tail = n 
      self.length += 1


    def add_to_head(self, value):
      n = Node(value)
      n.next_value = self.head
      self.head = n
      self.length += 1

    def remove_head(self):
      self.head = self.head.next_node
      self.length -= 1

    def remove_tail(self):
      current_node = self.head
      previous_node = None
      while current_node is not None:
        previous_node = current_node
        current_node = current_node.next_node
      else:
        previous_node.next_node = None
        self.length -= 1



class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    pass
