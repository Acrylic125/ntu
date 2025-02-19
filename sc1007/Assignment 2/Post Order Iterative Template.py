class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

def push(stack, node):
   temp = StackNode(node)
   if stack.top is None:
       stack.top = temp
       temp.next = None
   else:
       temp.next = stack.top
       stack.top = temp

def pop(stack):
   if stack.top is not None:
       temp = stack.top
       stack.top = temp.next
       return temp.data
   return None

def is_empty(stack):
   return stack.top is None

def peek(stack):
    if stack.top is not None:
        return stack.top.data
    return None

def postOrderIterativeS1(root: BSTNode):
    stack = Stack()
    cur = root
    last_printed = None
    while True:
        while cur != None:
            push(stack, cur)
            cur = cur.left 
        cur = pop(stack) 
        assert cur != None
        print(cur.data, end=" ")
        last_printed = cur
        if is_empty(stack):
            return
        parent = peek(stack)
        assert parent != None
        # This is to check if the traversal should go back up or go to the right.
        if parent.right != last_printed:
            cur = parent.right 
        else:
            # None here implies, dont look to the left.
            cur = None

if __name__ == "__main__":
   root = None
   choice = 1
   d = [20, 15, 50, 10, 18, 25, 80]
   # d = [20, 15, 50, 10, 18]
   for i in d:
       root = insert(root, i)

   print("1: Insert an integer into the binary search tree")
   print("2: Print the post-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("Post-order traversal: ", end="")
           postOrderIterativeS1(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")
