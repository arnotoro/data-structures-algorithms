class Node:
    def __init__(self, key: int):
        self.key = key
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
        if key < node.key:
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
        elif node.key > key:
            return self.search_help(node.left, key)
        elif node.key < key:
            return self.search_help(node.right, key)
        return True
    
    def preorder(self):
        if self.root is not None:
            self.preorder_help(self.root)    
        print("\t")
        
    def preorder_help(self, node):
        if node is not None:
            print(node.key, end=" ")
            self.preorder_help(node.left)
            self.preorder_help(node.right)

    def remove(self, key):
        return self.remove_help(self.root, key)

    def remove_help(self, node, key):
        if node is None:
            return node
        elif node.key > key:
            node.left = self.remove_help(node.left, key)
        elif node.key < key:
            node.right = self.remove_help(node.right, key)
        else:
            if node.left is None:
                node.temp = node.right
                node.key = None
                return node.temp
            elif node.right is None:
                node.temp = node.left
                node.key = None
                return node.temp
            else:
                node.temp = self.getMax(node.left)
                node.key = node.temp
                node.left = self.deleteMax(node.left)
        return node


    def getMax(self, node):
        if node.right is None:
            return node.key
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
            keys.append(cursor.key)

            if cursor.left is not None:
                que.append(cursor.left)
            if cursor.right is not None:
                que.append(cursor.right)

        for i in keys:
            print(i, end= " ")
        
        print("\t")

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6