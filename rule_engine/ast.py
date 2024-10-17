#ast.py
class Node:
  def __init__(self,type,left=None,right=None,value=None):
    self.type=type
    self.lft=left
    self.right=right
    self.value=value
