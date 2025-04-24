class Node:
    def __init__(self, key: int):
        self.data = key
        self.right = self.left = None
        self.temp = None

 
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_help(self.root, key)
    
    def insert_help(self, node, key):
        if key < node.data:
            if node.left:
                self.insert_help(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self.insert_help(node.right, key)
            else:
                node.right = Node(key)
        
    def search(self, key):
        return self.search_help(self.root, key)

    def search_help(self, node, key):
        if node is None:
            return False
        elif node.data > key:
            return self.search_help(node.left, key)
        elif node.data < key:
            return self.search_help(node.right, key)
        return True
    
    def preorder(self):
        if self.root is not None:
            self.preorder_help(self.root)    
        print()
        
    def preorder_help(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_help(node.left)
            self.preorder_help(node.right)

    def remove(self, key):
        return self.remove_help(self.root, key)

    def remove_help(self, node, key):
        if node is None:
            return node
        elif node.data > key:
            node.left = self.remove_help(node.left, key)
        elif node.data < key:
            node.right = self.remove_help(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self.getMax(node.left)
            node.left = self.remove_help
        return node


    def getMax(self, node):
        if node.right is None:
            return node.data
        return self.getMax(node.right)


    def deleteMax(self, node):
        if node.right is None:
            return node.left
        else:
            node.right = self.deleteMax(node.right)
            return node


    def breadthfirst(self):
        if self.root is None:
            return False
        
        que = [self.root]
        keys = []

        while len(que) > 0:
            cursor = que.pop(0)
            keys.append(cursor.data)

            if cursor.left is not None:
                que.append(cursor.left)
            if cursor.right is not None:
                que.append(cursor.right)

        for i in keys:
            print(i, end= " ")
        
        print("\t")

    def postorder(self):
        if self.root is not None:
            self.postorder_help(self.root)
        print()

    def  postorder_help(self, node):
        if node is not None:
            self.postorder_help(node.left)
            self.postorder_help(node.right)
            print(node.data, end=" ")

    def inorder(self):
        if self.root is not None:
            self.inorder_help(self.root)
        print()
    
    def inorder_help(self, node):
        if node is not None:
            self.inorder_help(node.left)
            print(node.data, end=" ")
            self.inorder_help(node.right)

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()        # 2 4 3 1 6 7 9 5 
    Tree.inorder()          # 1 2 3 4 5 6 7 9  
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6
