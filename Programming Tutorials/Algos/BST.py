class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursively(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursively(node.right, key)
        return node

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.key == key:
            return key  # Return the key instead of the node object
        if key < node.key:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    # Rest of the code remains unchanged...

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursively(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.key = temp.key
            node.right = self._delete_recursively(node.right, temp.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node, result):
        if node:
            self._inorder_traversal_recursively(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursively(node.right, result)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(18)

    res = bst.inorder_traversal()
    low,high = 7,15
    ans = 0
    for i in res:
        if low <= i <= high:
            ans += i
    print(ans)

    # print("Search for key 60:", bst.search(60))
    # print("Search for key 90:", bst.search(90))

    # bst.delete(30)
    # print("Inorder Traversal after deleting 30:", bst.inorder_traversal())
