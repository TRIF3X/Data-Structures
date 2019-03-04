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
      # if our length is less than 2 we don't have a head or a tail just a node
      if self.length < 2:
        return None
      else:
        self.head = self.head.next_node
        self.length -= 1

    def remove_tail(self):
      # if our length is less than 2 we don't have a head or a tail just a node
      if self.length < 2:
        return None
      else:
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
    self.size += 1
    pass
  
  def dequeue(self):
    self.size -= 1
    pass

  def len(self):
    return self.size
