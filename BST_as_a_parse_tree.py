class Node:
    def __init__(self, data = None):
        self.key = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def put_helper(self, x, key):
        if x is None:
            return Node(key)
        else :
            cmp = key < x.key
            if cmp < 0:
                x.left = self.put_helper(x.left, key)
            elif cmp > 0:
                x.right = self.put_helper(x.right, key)
            else:
                x.key = key
            return x
    def put(self, key):
        self.root = self.put_helper(self.root, key)
    def inorder_helper(x, q):
        inorder_helper(x.left)
        q.append(x.key)
        inorder_helper(x.right)
    
       
st = BST()
st.put(1)
st.put(2)

