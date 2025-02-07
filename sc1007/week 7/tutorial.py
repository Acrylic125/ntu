from typing import List, Any

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

def printInorder(tree: List[Any]):
    depth = 0
    length_remainder = len(tree)

    while length_remainder != 0:
        depth += 1
        length_remainder = length_remainder >> 1
    
    for i in range(0, depth):
        

    i = 0
    r = 1 << i

printPreOrderTree([1, 2, 3, 4, 5, 6, 7])
