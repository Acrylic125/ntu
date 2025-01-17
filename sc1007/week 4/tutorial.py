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
        l = []
        while (cur != None):
            l.append(cur.value)
            cur = cur.next
        print(l)

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

def move_max_to_front(ll: LinkedList):
    if (ll.first == None):
        return

    targetLinkPrev: LinkedListLink | None = None
    targetLink: LinkedListLink = ll.first

    highest = targetLink.value
    prev: LinkedListLink | None = None
    cur = ll.first
    while (cur != None):
        if (cur.value > highest):
            highest = cur.value
            targetLink = cur
            targetLinkPrev = prev
        prev = cur
        cur = cur.next

    if (targetLinkPrev != None):
        targetLinkPrev.next = targetLink.next
        targetLink.next = ll.first
        ll.first = targetLink

def remove_duplicates_sorted_ll(ll: LinkedList):
    if (ll.first == None):
        return
    prev: LinkedListLink = ll.first
    cur = ll.first
    while (cur != None):
        if (cur.value != prev.value):
            prev.next = cur
            prev = cur
        cur = cur.next
    prev.next = None

print("Part 1")
print("Before move:")
ll = LinkedList(
        list(range(0, 11, 1))
        )
ll.print()
print("After move:")
move_even_items_to_back(ll)
ll.print()

print("Part 2")
print("Before move:")
ll = LinkedList(
        [1, 49, 69, 1000, 39, 568, 20, 420]
        )
ll.print()
print("After move:")
move_max_to_front(ll)
ll.print()

print("Part 3")
print("Before remove:")
ll = LinkedList(
        [1, 1, 2, 3, 4, 4, 5, 5]
        )
ll.print()
print("After remove:")
remove_duplicates_sorted_ll(ll)
ll.print()

