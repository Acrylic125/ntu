class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def hasGreatGrandchild(node):
    left_height = hasGreatGrandchild(node.left) if node.left != None else 0
    right_height = hasGreatGrandchild(node.right) if node.right != None else 0

    total_height = max(left_height, right_height) + 1
    if total_height > 3:
        print(node.item, end=" ")
    return total_height

    # queue = []
    # if node.right != None:
    #     cur = node.right
    #     queue.append(cur)
    #     hasGreatGrandchild(cur)
    # if node.left != None:
    #     cur = node.left
    #     queue.append(cur)
    #     hasGreatGrandchild(cur)
    # if len(queue) <= 0:
    #     return False
    #
    # level = 0
    # first_in_level = None 
    # while len(queue) > 0:
    #     cur = queue.pop(0)
    #     if first_in_level != None and cur == first_in_level:
    #         first_in_level = None
    #         level += 1
    #     if cur.right != None:
    #         if first_in_level == None: 
    #             first_in_level = cur.right
    #         queue.append(cur.right)
    #     if cur.left != None:
    #         if first_in_level == None: 
    #             first_in_level = cur.left
    #         queue.append(cur.left)
    # if level >= 2:
    #     print(node.item, end=" ")
    #     return True
    # return False 

# Write your code here #

if __name__ == "__main__":
    # Create a tree with nodes having great-grandchildren
    root = BTNode(1)
    
    # Left subtree
    root.left = BTNode(2)
    root.left.left = BTNode(4)
    root.left.left.left = BTNode(8)
    root.left.left.left.left = BTNode(16)
    
    # Right subtree  
    root.right = BTNode(3)
    root.right.right = BTNode(7)
    root.right.right.right = BTNode(15)
    root.right.right.right.right = BTNode(31)

    print("Visual representation of the tree:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    
    print("\nNodes with great-grandchildren:", end=" ")
    hasGreatGrandchild(root)
    print()
