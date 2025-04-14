class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        return None

    def is_empty(self):
        return len(self.items) == 0

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling
        if curr and curr.char == char:
            return curr
        return None

    def _insert_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        if curr and curr.char == char:
            return curr  # already exists

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:
            node.first_child = new_node
        return new_node

    def insert(self, word):
        current = self.root
        for char in word:
            child = self._insert_child(current, char)
            current = child
        current.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False  # Character path not found
        return node.is_end_of_word


def count_in_range(trie, L, R):
    def _count_in_range(node, L, R, on_bounds_min=True, on_bounds_max=True, debug_str=""):
        count = 0
        debug_str = f"{debug_str}{node.char}"

        l_first_char = L[0] if len(L) > 0 else ""
        r_first_char = R[0] if len(R) > 0 else ""

        if on_bounds_max and r_first_char == "":
            # print(f"T1 {debug_str} {node.char}")
            return count
        if l_first_char != "" and node.char < l_first_char and on_bounds_min:
            # print(f"T2 {debug_str} {node.char}")
            return count
        if r_first_char != "" and node.char > r_first_char and on_bounds_max:
            # print(f"T3 {debug_str} {node.char}")
            return count
        
        if on_bounds_max and node.char != r_first_char:
            on_bounds_max = False
        if on_bounds_min and (node.char != l_first_char or l_first_char == ""):
            on_bounds_min = False

        cur = node.first_child
        if node.is_end_of_word and len(L) <= 1:
            count = count + 1
        while cur != None:
            count = count + _count_in_range(cur, L[1:], R[1:], on_bounds_min, on_bounds_max, debug_str)
            cur = cur.next_sibling
        return count

    count = 0
    cur = trie.root.first_child
    while cur != None:
        count = count + _count_in_range(cur, L, R, True, True)
        cur = cur.next_sibling
    return count
        

# st = [
#         "5 1",
#         'cat',
#         'carry',
#         'camera',
#         'damage',
#         'dog',
#         # "damage dog",
#         # "can cat",
#         "can dog",
#         # "what wheef"
#         ]
# print("fuck" < "you")


#Read input
st = [
        '5 4',
        'cat',
        'car',
        'care',
        'camera',
        'dog',
        'car cart',
        'a d',
        'care care',
        "dog dog",
        ]
# st = [
#         '5 4',
#         'app',
#         'apple',
#         'bat',
#         'boo',
#         'aereospace',
#         'app bat',
#         'a d',
#         'care care',
#         "dog dog",
#         ]
n, q = map(int, st[0].split())
trie = Trie()
st = st[1:]

# Insert words
for i in range(n):
    word = st[i].strip()
    trie.insert(word)

st = st[n:]

# Process queries
for i in range(q):
    L, R = st[i].strip().split()
    print(count_in_range(trie, L, R))

