#  Tuesday

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.left and self.right and self.value is None:
      self.value = value
    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    pass

  def get_max(self):
    # traverse to the right until we can no longer move right, if we hit None we know the node above it is the max
    while self.right is not None:
      self.right
    if self.right == None:
      return self.value


t = BinarySearchTree(30)
t.insert(20)
t.insert(25)
t.insert(50)
t.insert(77)
t.insert(92)
print(t.get_max())

