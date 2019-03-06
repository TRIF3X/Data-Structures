# Wednesday

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) -1)

  def delete(self):
    self.storage.insert(0, self.storage.pop())
    self.storage.pop(1)
    self._sift_down(0)

  def get_max(self):
    # If stored in an array, our first value is the 'root' which means it is the biggest value
    return self.storage[0]

  def get_size(self):
    # return the length of the storage
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2

    if self.storage[parent] < self.storage[index]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        self._bubble_up(parent)


  def _sift_down(self, index):
    left_child = (index * 2) + 1
    right_child = (index * 2) + 2
    parent = (index - 1) // 2
    # if the left node is greater than the right node, check left node against parent node. If child node has higher value swap them
    if self.storage[left_child] > self.storage[right_child]:
      if self.storage[left_child] > self.storage[parent]:
        self.storage[left_child], self.storage[parent] = self.storage[parent], self.storage[left_child]
    elif self.storage[right_child] > self.storage[left_child]:
      if self.storage[right_child] > self.storage[parent]:
        self.storage[right_child], self.storage[parent] = self.storage[parent], self.storage[right_child]
