def reverse_stack(stack: list):
    queue = []

    while (len(stack) > 0):
        queue.append(stack.pop())

    while (len(queue) > 0):
        stack.append(queue.pop(0))

def reverse_first_k_items(queue: list, k: int):
    reversed_stack = []
    positioned_queue = []

    maxK = min(k, len(queue))
    for _ in range(0, maxK):
        reversed_stack.append(queue.pop(0))
    while (len(queue) > 0):
        positioned_queue.append(queue.pop(0))

    while (len(reversed_stack) > 0):
        queue.append(reversed_stack.pop())
    while (len(positioned_queue) > 0):
        queue.append(positioned_queue.pop(0))

def sort_stack(stack: list):
    sorted_queue = []

    while (len(stack) > 0):
        lo = min(stack)
        
        add_back_stack = []
        while (True):
            entry = stack.pop()
            if entry == lo:
                sorted_queue.append(entry)
                break
            add_back_stack.append(entry) 

        while (len(add_back_stack) > 0):
            stack.append(add_back_stack.pop())

    while (len(sorted_queue) > 0):
        stack.append(sorted_queue.pop(0))

stack = [1, 2, 3, 4, 5]
print("--------")
print(stack)
print("Reverse")
reverse_stack(stack)
print(stack)
print("Reverse again")
reverse_stack(stack)
print(stack)

queue = [1, 2, 3, 4, 5]
print("--------")
print(queue)
print("Reverse first 3")
reverse_first_k_items(queue, 3)
print(queue)
print("Reverse first 4")
reverse_first_k_items(queue, 4)
print(queue)

stack = [5, 4, 3, 2, 1]
print("--------")
print(stack)
print("Sorted")
sort_stack(stack)
print(stack)
print(" ")
stack = [3, 4, 2, 1, 8, 2, 2, 4, 9, 0]
print(stack)
print("Sorted")
sort_stack(stack)
print(stack)


