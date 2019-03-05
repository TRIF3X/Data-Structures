#  Tuesday

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    bst = BinarySearchTree(value)
    if bst.left and bst.right is None:
      root = bst
    else:
      while bst.left or bst.right is not None:


  def contains(self, target):
    pass

  def get_max(self):
    # traverse to the right until we can no longer move right, if we hit None we know the node above it is the max
    while self.right != None:
      self.right
    return self.value
