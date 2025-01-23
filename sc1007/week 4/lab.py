class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

def printList(head):
    print("Current List:", end=" ")
    cur = head
    while cur is not None:
        print(cur.item, end=" ")
        cur = cur.next
    print()

def findNode(head, index):
    if head is None or index < 0:
        return None
    cur = head
    while index > 0:
        cur = cur.next
        if cur is None:
            return None
        index -= 1
    return cur

def insertNode(ptrHead, index, value):
    newNode = ListNode(value)
    if ptrHead is None:
        return newNode
    if index == 0:
        newNode.next = ptrHead
        return newNode
    cur = ptrHead
    prev = None
    count = 0
    while cur is not None and count < index:
        prev = cur
        cur = cur.next
        count += 1
    if prev is not None:
        prev.next = newNode
        newNode.next = cur
    return ptrHead

def removeNode(head, index):
    i = 0
    prev = None
    next = head
    while next != None:
        if i == index:
            if prev != None:
                prev.next = head.next
            return 1
        prev = head
        next = head.next
    return 0


if __name__ == "__main__":
    head = None
    size = 0
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    while True:
        try:
            item = int(input())
            head = insertNode(head, size, item)
            size += 1
        except ValueError:
            break
    printList(head)
    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            head = removeNode(head, index)
            size -= 1
            print("After the removal operation:")
            printList(head)
        except ValueError:
            break
    printList(head)
