class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree(object):
    def insert(self, root, node):
        if root is None:
            return node

        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)

        return root


    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print (root.val)


def post_order(nodeList):
  r = Node(nodeList[0])
  node = BinarySearchTree()
  for nd in nodeList:
      node.insert(r, Node(nd))
  print ("------Post order ---------")
  print (node.post_order_place(r))


print(post_order([30,24,5,28,45,98,52,60]))