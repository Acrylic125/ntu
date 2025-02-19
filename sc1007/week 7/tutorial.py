from typing import List, Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
   
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
           
        new_node = Node(data)
       
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
       
        prev_node = self.findNode(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def removeNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre.next is not None:
            pre.next = pre.next.next
            self.size -= 1
            return True
        return False
        
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

class Stack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, data):    
        self.ll.insertNode(data, 0)
        
    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        self.ll.removeNode(0)
        return data
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    
        
    def isEmpty(self):
        return self.ll.size == 0
        
    def getSize(self):
        return self.ll.size
        
    def printStack(self):
        self.ll.printList()

class Queue:
    def __init__(self):
        self.ll = LinkedList()
        
    def enqueue(self, data):    
        self.ll.insertNode(data, self.ll.size)
        
    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        self.ll.removeNode(0)
        return data
        
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.ll.head.data    
        
    def getSize(self):           
        return self.ll.size
        
    def isEmpty(self):
        return self.ll.size == 0
    
    def printQueue(self):
        self.ll.printList()


class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def printPreOrderTree(tree: List[Any]):
    i = 0
    r = 1 << i

    tl = []
    index = 0
    while index < len(tree):
        tl.append(tree[index]) 

        index += 1
        r -= 1
        if r <= 0:
            i += 1
            r = 1 << i
            print(tl)

            tl = []
    
    if len(tl) > 0:
        print(tl)

def levelOrderTraversal(root: BSTNode):
    queue = Queue()

    cur = root 
    queue.enqueue(root)
    first = None
    while cur != None: 
        if queue.isEmpty():
            return
        cur = queue.dequeue()     
        if first == cur:
            first = None
        assert cur != None 
        print(cur.data, end=" ")
        if cur.left != None:
            queue.enqueue(cur.left)
            if first == None: 
                first = cur.left
        if cur.right != None:
            queue.enqueue(cur.right)
            if first == None: 
                first = cur.right

def preOrderIterative(root: BSTNode):
    stack = Stack()
    stack.push(root)
    
    cur = root 
    while not stack.isEmpty():
        cur = stack.pop()
        assert cur != None
        print(cur.data, end=" ") 
        if cur.right != None:
            stack.push(cur.right)
        if cur.left != None:
            stack.push(cur.left)

def maxDepth(root: BSTNode):
    depth = 0
    queue = Queue()

    queue.enqueue(root)
    
    first = None
    while not queue.isEmpty():
        cur = queue.dequeue()
        if first == cur:
            depth += 1
            first = None 
        if cur.left != None:
            if first == None:
                first = cur.left
            queue.enqueue(cur.left)
        if cur.right != None:
            if first == None:
                first = cur.right
            queue.enqueue(cur.right)
    return depth

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

root = None

d = [20, 15, 50, 10, 18, 25, 80]
for i in d:
    root = insert(root, i)

print("On level ordering")
levelOrderTraversal(root)

print("Pre ordering")
preOrderIterative(root)

d = [20, 15, 50, None, None, 10, 18, 25, 80, None, None]
for i in d:
    root = insert(root, i)

print("Max depth")
print(maxDepth(root))

