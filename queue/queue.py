# Monday

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

class Linked_list:
  def __init__(self, head, tail, length):
    self.head = head
    self.tail = tail
    self.length = length

    def add_to_tail(self, value):
      pass

    def add_to_head(self, value):
      pass

    def remove_head():
      pass

    def remove_tail():
      pass

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
