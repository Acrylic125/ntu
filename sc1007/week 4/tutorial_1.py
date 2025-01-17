from typing import List, Any


class LinkedListLink:
    value: int = 0
    next: Any = None

class LinkedList:
    first: LinkedListLink | None = None

    def __init__(self, values: List[int]) -> None:
        prev: LinkedListLink | None = None
        for v in values:
            node = LinkedListLink()
            node.value = v
            if prev == None:
                self.first = node 
            else:
                prev.next = node
            prev = node

    def print(self):
        cur = self.first
        while (cur != None):
            print(cur.value)
            cur = cur.next

def move_even_items_to_back(ll: LinkedList):
    while True:
        targetLinkPrev: LinkedListLink | None = None 
        targetLink: LinkedListLink | None = None 

        prev: LinkedListLink | None = None
        cur = ll.first
        shouldPush = False
        while (cur != None):
            if (cur.value % 2 == 1):
                if (targetLink != None):
                    shouldPush = True
            else:
                if (targetLink == None):
                    targetLinkPrev = prev
                    targetLink = cur
            prev = cur
            cur = cur.next

        if (shouldPush and targetLink != None and prev != None):
            if (targetLinkPrev == None):
                ll.first = targetLink.next
            else:
                targetLinkPrev.next = targetLink.next
            targetLink.next = None
            prev.next = targetLink 
        else:
            return

ll = LinkedList(
        list(range(0, 11, 1))
        )
ll.print()
print("After move:")
move_even_items_to_back(ll)
ll.print()
