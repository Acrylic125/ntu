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
    
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

def moveMinNode(head):
    min_value = None
    cur = head 
    while cur != None:
        if min_value == None or cur.data < min_value:
            min_value = cur.data
        cur = cur.next
    if min_value == None:
        return head

    cur = head 
    prev = None
    min_node_head: Node | None = None
    min_node_chain: Node | None = None
    
    main_node_head: Node | None = None
    main_node_chain: Node | None = None
    while cur != None:
        if cur.data == min_value:
            if min_node_head == None:
                min_node_head = cur 
            elif min_node_chain != None: 
                min_node_chain.next = cur
            else: 
                print("Unexpected no min node chain.")
            min_node_chain = cur
            cur = cur.next
            min_node_chain.next = None
        else:
            if main_node_head == None:
                main_node_head = cur 
            elif main_node_chain != None: 
                main_node_chain.next = cur
            else: 
                print("Unexpected no main node chain.")
            main_node_chain = cur
            cur = cur.next
            main_node_chain.next = None
    if min_node_head != None:
        min_node_chain.next = main_node_head
        return min_node_head
    return main_node_head

if __name__ == "__main__":
    linked_list = LinkedList()
    
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
    
    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break
    
    print("\nBefore:", end=" ")
    linked_list.printList()
    
    linked_list.head = moveMinNode(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()
