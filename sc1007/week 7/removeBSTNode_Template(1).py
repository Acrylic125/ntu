class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

def insertBSTNode(root, value):
    """ Recursive approach to insert a node into a BST. """
    if root is None:
        return BTNode(value)
    
    if value < root.item:
        root.left = insertBSTNode(root.left, value)
    elif value > root.item:
        root.right = insertBSTNode(root.right, value)
    return root  # Ensure the modified node is returned

def findMin(node):
    """ Find the node with the smallest value in a subtree. """
    while node.left is not None:
        node = node.left
    return node

def removeBSTNode(node, value):
    parent: BTNode | None = None 
    node_to_delete: BTNode | None = None 
    
    parent = None
    cur = node 
    while cur != None:
        if value == cur.item:
            node_to_delete = cur
            break
        parent = cur
        if value < cur.item:
            cur = cur.left
        else:
            cur = cur.right

    if node_to_delete == None:
        return 1
    if parent == None: 
        raise RuntimeError("Tree needs at least 2 levels.")

    child_side = -1 if parent.left == node_to_delete else 1

    left: BTNode | None = node_to_delete.left
    right: BTNode | None = node_to_delete.right

    # No child
    if left == None and right == None:
        if child_side >= 0:
            parent.right = None
        else:
            parent.left = None
        return 0

    # 1 child
    if left == None and right != None:
        if child_side >= 0:
            parent.right = right
        else:
            parent.left = right
        return 0
    if left != None and right == None:
        if child_side >= 0:
            parent.right = left
        else:
            parent.left = left
        return 0

    # 2 Child :w
    successor_parent = node_to_delete
    successor: BTNode = right
    while successor.left != None:
        successor_parent = successor
        successor = successor.left
    print(f"{successor_parent.item} {successor.item}")
    if successor == right:
        node_to_delete.item = successor.item
        node_to_delete.right = None
    else:
        node_to_delete.item = successor.item
        successor_parent.left = successor.right
    #     node_to_delete.right = None
    # else:
    #     node_to_delete.item = successor.item 
    #     successor_parent.left = successor.right

    return 0

# def removeBSTNode(node, value):
#     if node.item == value:
#         # No child case.
#         if node.left == None and node.right == None:
#             return None 
#         
#         # 1 child case.
#         if node.left == None and node.right != None:
#             return node.right
#         if node.left != None and node.right == None:
#             return node.left
#     
#         # 2 child case 
#         parent = None
#         successor = node.right
#         while successor.left != None:
#             parent = successor
#             successor = successor.left
#         if parent != None:
#             parent.left = successor.right 
#         successor.left = node.left
#         successor.right = node.right
#         return successor
#
#     if node.left != None and value <= node.left.item:
#         node.left = removeBSTNode(node.left, value)
#     if node.right != None and value <= node.right.item:
#         node.right = removeBSTNode(node.right, value)
#     return node


def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.item, end=" ")
        printBSTInOrder(node.right)

def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

if __name__ == "__main__":
    root = None
    root = BTNode(item=100)
    root.left = BTNode(item=50)
    root.left.left = BTNode(item=25)
    root.left.left.left = BTNode(item=12)
    root.left.left.right = BTNode(item=32)
    root.left.right = BTNode(item=75)
    root.left.right.left = BTNode(item=62)
    root.left.right.right = BTNode(item=80)
    root.right = BTNode(item=150)
    root.right.left = BTNode(item=125)
    root.right.right = BTNode(item=175)
    print("Binary Search Tree Node Removal Program")
    print("=====================================")
    
    print("\nFirst, let's build the BST:")
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            print("\nIn-order traversal: ", end="")
            printBSTInOrder(root)
            print()
            
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nNow let's remove nodes:")
    while True:
        try:
            value = input("\nEnter a value to remove (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            result = removeBSTNode(root, i)
            result = 0
            if result == 0:
                print("\nBST structure after removal:")
                printTree(root)
                print("\nIn-order traversal: ", end="")
                printBSTInOrder(root)
                print()
            else:  # result == -1
                print("Value not found in the tree!")
            
        except ValueError:
            print("Invalid input! Please enter an integer.")
