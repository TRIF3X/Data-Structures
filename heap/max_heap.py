# Wednesday

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) -1)

  def delete(self):
    top_item = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) -1]
    self.storage.pop()
    self._sift_down(0)
    return top_item

  def get_max(self):
    # If stored in an array, our first value is the 'root' which means it is the biggest value
    return self.storage[0]

  def get_size(self):
    # return the length of the storage
    return len(self.storage)

  def _bubble_up(self, index):
    while self.storage[(index - 1) // 2] < self.storage[index] and index > 0:
      self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index - 1) // 2]
      index = (index - 1) // 2


  def _sift_down(self, index):
    # if the left node is greater than the right node, check left node against parent node. If child node has higher value swap them
    while index * 2 + 1 <= len(self.storage) -1:
      if index * 2 + 2 > len(self.storage) -1:
        big_num = index * 2 + 1
      elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
        big_num = index * 2 + 1
      else:
        big_num = index * 2 + 2

      # handle swaps after we've determined which is bigger
      if self.storage[big_num] > self.storage[index]:
        self.storage[big_num], self.storage[index] = self.storage[index], self.storage[big_num]
      index = big_num


# keys:
#     left_child = (index * 2) + 1
#     right_child = (index * 2) + 2
#     parent = (index - 1) // 2