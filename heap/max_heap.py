# Wednesday

class Heap:
  def __init__(self, parent):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    # If stored in an array, our first value is the 'root' which means it is the biggest value
    return self.storage[0]

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass



# key:
# left_child: (index * 2) + 1
# right_child: (index * 2) + 2
# parent: (index - 1) // 2