class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node

class Linked_list:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail
    self.length = 0

  def add_to_tail(self, value):
    n = Node(value)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      self.tail.next_node = n
      self.tail = n 
    self.length += 1


  def add_to_head(self, value):
    n = Node(value)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      n.next_node = self.head
      self.head = n
    self.length += 1

  def remove_head(self):
    if not self.head:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
      self.length -= 1
      return self.head
    else:
      current_head = self.head
      self.head = self.head.next_node
      self.length -= 1
      return current_head


  def remove_tail(self):
    # if our length is less than 2 we don't have a head or a tail just a node
    if not self.tail:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
      self.length -= 1
      return self.tail
    else:
      current_node = self.head
      previous_node = None
      while current_node.next_node is not None:
        previous_node = current_node
        current_node = current_node.next_node
      removed = current_node
      if previous_node is not None:
        self.tail = previous_node
      self.tail.next_node = None
      return removed.value
      self.length -= 1




class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = Linked_list()

  def enqueue(self, item):
    n = Node(item)
    self.size += 1
    self.storage.add_to_head(n)
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      removed = self.storage.remove_tail()
      return removed.value
    else:
      return None

  def len(self):
    return self.size

